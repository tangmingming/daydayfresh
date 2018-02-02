import os
from urllib.parse import urlparse, parse_qs

from django.shortcuts import render
from django.db.models.query import F
from django.contrib.auth import get_user_model
from django.views import View
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.authentication import SessionAuthentication

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.conf import settings
from . import models
from .serializers import ShopCardMercSerialize, ShopCardMercDetailSerialize, OrderSerialize, OrderMercSerialize, AlipayCallBackSerialize
from utils.permissions import GetOrderPermission
from utils.alipay import AliPay
# Create your views here.

User = get_user_model()
alipay = AliPay(
  appid="2016082600316878",
  app_notify_url="daydayfresh.mingmingt.xyz",
  app_private_key_path=os.path.join(settings.BASE_DIR, "apps/transact/keys/app_private_key.txt"),
  alipay_public_key_path=os.path.join(settings.BASE_DIR, "apps/transact/keys/alipay_public_key.txt"),  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
  debug=True,  # 默认False,
  return_url="daydayfresh.mingmingt.xyz/pay/alipaycallback"
)

class ShoppingCardMercViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,  mixins.DestroyModelMixin, GenericViewSet):
  queryset = models.ShoppingCardMerc.objects.all()
  serializer_class = ShopCardMercSerialize
  authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
  permission_classes = (permissions.IsAuthenticated, )

  def list(self, request, *args, **kwargs):
    queryset = self.get_queryset().filter(user=request.user)

    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    if self.get_queryset().filter(user=request.user).count() > 30:
      raise ParseError("老板 购物车装不下了。。。")
    queryset = self.get_queryset().filter(user=request.user, merchandise_id=serializer.validated_data["merchandise"])
    if queryset:
      queryset[0].num=F("num")+serializer.validated_data["num"]
      queryset[0].save()
    else:
      serializer.validated_data["user"] = request.user
      serializer.save()
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def get_serializer_class(self):
    assert self.serializer_class is not None, (
      "'%s' should either include a `serializer_class` attribute, "
      "or override the `get_serializer_class()` method."
      % self.__class__.__name__
    )

    return ShopCardMercDetailSerialize if self.action in ["list", "retrieve"] else ShopCardMercSerialize
#
# s = ShopCardMercSerialize()
# s.get_qu

class OrderViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
  serializer_class = OrderSerialize
  queryset = models.OrderMerc.objects.all()
  permission_classes = (permissions.IsAuthenticated, GetOrderPermission)

  def get_queryset(self):
    return models.Order.objects.filter(user=self.request.user)

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data["user"] = request.user
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class OrderMercViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
  queryset = models.OrderMerc.objects.all()
  serializer_class = OrderMercSerialize
  permission_classes = (permissions.IsAuthenticated, )
  def list(self, request, *args, **kwargs):
    try:
      order = request.query_params["order"][0]
    except:
      raise ParseError("you must provide th order number!")
    queryset = self.queryset.filter(order=order)
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data["unit_price"] = serializer.validated_data["merchandise"].sale_price
    self.perform_create(serializer)
    models.ShoppingCardMerc.objects.filter(user=request.user, merchandise=serializer.validated_data["merchandise"]).delete()
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AlipaySyncReturn(View):
  def get(self, request, *args, **kwargs):
    full_path = request.get_full_path()
    o = urlparse(full_path)
    query = parse_qs(o.query)
    processed_query = {}
    ali_sign = query.pop("sign")[0]
    for key, value in query.items():
      processed_query[key] = value[0]
    if not alipay.verify(processed_query, ali_sign):
      return HttpResponseBadRequest("error")
    return HttpResponseRedirect("beijing")

class AlipayAsynNoti(View):
  def post(self, request, *args, **kwargs):
    app_id = request.POST.get("app_id", None)
    if app_id != settings.PAY["alipay"]["app_id"]:
      return HttpResponseBadRequest("app_id error")
    sign = request.POST.pop("sign", None)
    if not alipay.verify(request.POST, sign):
      return HttpResponseBadRequest("sign error")
    out_trade_no = request.POST["out_trade_no"]
    orders = models.Order.objects.filter(id=out_trade_no)
    for order in orders:
      order.status = 1
      orders.pay_sn = request.POST["trade_no"]

    return HttpResponse("success")
