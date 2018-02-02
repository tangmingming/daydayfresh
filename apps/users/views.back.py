import logging
import json
from datetime import datetime, timedelta

from django.conf import settings

from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.exceptions import ValidationError, ParseError
from rest_framework import status
from rest_framework import mixins

from . import serializers
from . import models
from utils.sms import Sms

# Create your views here.

logger = logging.getLogger(__file__)

class VerifyCodeViewSet(viewsets.ViewSet):
    """
    send and check sms verify code
    """
    sms = Sms()
    INVIDITY_PERIOD = settings.SMS["validity_period"]
    #check验证码
    def list(self, request):
        verify_code_ser = serializers.VerifyCodeSerialize(data=request.data)
        verify_code_ser.is_valid(raise_exception=True)
        mobile = request.data["mobile"]
        code = request.data["code"]
        query_sets = models.VerifyCode.objects.filter(mobile=mobile).order_by("-send_time")
        if not len(query_sets):
            return ParseError("手机没有发送验证码记录")
        if query_sets[0].code != code:
            return ParseError("验证码错误")
        last_time = query_sets[0].send_time
        interval = datetime.now() - last_time
        if interval.total_seconds() > 60 * self.INVIDITY_PERIOD:
            return ParseError("验证码已过期,请重新发送")

        return Response("验证通过")


    def create(self, request):
        if "mobile" not in request.data:
            raise ParseError("手机号码错误")
        verify_code_ser = serializers.VerifyCodeSerialize(data=request.data, partial=True)
        verify_code_ser.is_valid(raise_exception=True)
        mobile = request.data["mobile"]
        query_sets = models.VerifyCode.objects.filter(mobile=mobile).order_by("-send_time")
        if len(query_sets):
            last_time = query_sets[0].send_time
            interval = datetime.now() - last_time
            if interval.total_seconds() > 60:
                return ParseError("距离上次发送不到60秒")

        code = self.sms.send_verifycode(mobile)
        if code == None:
            raise ParseError("发送失败,请稍后再试!")

        verify_code = models.VerifyCode(mobile=mobile, code=code)
        verify_code.save()

        return Response("发送成功")

# class VerifyCodeViewSet(viewsets.ModelViewSet):
#     #check验证码
#     queryset = models.VerifyCode.objects.all()
#     serializer_class = serializers.VerifyCodeSerialize

class ShopUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ShopUserSerialize
    queryset = models.ShopUser.objects.all()

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    INVIDITY_PERIOD = settings.SMS["validity_period"]
    def create(self, request):
        mobile = request.data.get("mobile", "")
        code = request.data.get("code", "")
        verify_code_data = {
            "mobile": mobile,
            "code": code,
        }
        verify_code_ser = serializers.VerifyCodeSerialize(data=verify_code_data)
        verify_code_ser.is_valid(raise_exception=True)
        shop_user_ser = serializers.ShopUserSerialize(data=request.data)
        shop_user_ser.is_valid(raise_exception=True)
        query_sets = models.VerifyCode.objects.filter(mobile=mobile, send_time__gte=datetime.now()-timedelta(minutes=settings.SMS["validity_period"]))
        if not len(query_sets):
            return ParseError("手机没有发送验证码记录")
        is_right = False
        for i in query_sets:
            if code == i.code:
                is_right = True
                break

        if not is_right:
            return ParseError("验证码错误")
        self.perform_create(verify_code_ser)
        headers = self.get_success_headers(verify_code_ser.data)
        return Response(verify_code_ser.data, status=status.HTTP_201_CREATED, headers=headers)

class RegistryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
  pass
