
from rest_framework.serializers import ModelSerializer, ValidationError, Serializer
from rest_framework import serializers

from . import models

class ShopCardMercSerialize(ModelSerializer):

  class Meta:
    model = models.ShoppingCardMerc
    exclude = ("user", )

class ShopCardMercDetailSerialize(ModelSerializer):
  class Meta:
    model = models.ShoppingCardMerc
    exclude = ("user",)
    depth = 1


class OrderMercSerialize(ModelSerializer):
  class Meta:
    model = models.OrderMerc
    fields = "__all__"
    read_only_fields = ("unit_price", )

class OrderSerialize(ModelSerializer):

  class Meta:
    model = models.Order
    exclude = ("user", )


class AlipayCallBackSerialize(Serializer):
  app_id = serializers.CharField(max_length=32)
  method = serializers.CharField(max_length=128)
  sign_type = serializers.CharField(max_length=10)
  sign = serializers.CharField(max_length=256)
  charset = serializers.CharField(max_length=10)
  timestamp = serializers.DateTimeField()
  version = serializers.CharField(max_length=3)
  auth_app_id = serializers.CharField(max_length=32)

  out_trade_no = serializers.CharField(max_length=64)
  trade_no = serializers.CharField(max_length=64)
  total_amount = serializers.FloatField()
  seller_id = serializers.CharField(max_length=16)
