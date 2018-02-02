import logging
import json
from datetime import datetime, timedelta

from django.conf import settings

from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.exceptions import ValidationError, ParseError, APIException
from rest_framework import status
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from utils.sms import Sms
from utils.permissions import GetUserInfoPermisson, GetUpdatePermission


# Create your views here.

logger = logging.getLogger(__file__)


class VerifyCodeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    sms = Sms()

    serializer_class = serializers.VerifyCodeSerialize
    queryset = models.VerifyCode.objects.all()

    permission_classes = (GetUserInfoPermisson,)
    def create(self, request):
        serializer = serializers.VerifyCodeSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.data["mobile"]
        code = self.sms.send_verifycode(mobile)
        if code == None:
            raise ParseError("发送失败,请稍后再试!")
        verify_code = models.VerifyCode(mobile=mobile, code=code)
        verify_code.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class VerifyCodeViewSetb(viewsets.ViewSet):
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

class ShopUserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.ShopUserSerialize
    queryset = models.ShopUser.objects.all()
    permission_classes = (GetUserInfoPermisson, )


class ReceInfoViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
  serializer_class = serializers.ReceInfoSerialize
  queryset = models.ReceInfo.objects.all()
  permission_classes = (IsAuthenticated, GetUpdatePermission)
