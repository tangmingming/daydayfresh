from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Merchandise

# Create your models here.


User = get_user_model()

class ShoppingCardMerc(models.Model):
    """
    购物车商品
    """
    user = models.ForeignKey(User, verbose_name="用户")
    merchandise = models.ForeignKey(Merchandise, verbose_name="商品")
    num = models.IntegerField(verbose_name="数量")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")


class Order(models.Model):
    """
    订单
    """
    STATUS = (
        (0, "未支付"),
        (1, "已支付"),
        (2, "交易成功"),
        (3, "已取消"),
        (4, "已退款"),
        (10, "异常")
    )

    PAY_TYPE = (
        (0, "支付宝"),
        (1, "微信"),
    )

    LOGISTICS_STATUS = (
        (0, "未发货"),
        (1, "运输中"),
        (2, "已签收"),
        (3, "异常"),
    )

    user = models.ForeignKey(User, verbose_name="用户")
    status = models.SmallIntegerField(choices=STATUS, default=0, verbose_name="订单状态")
    message = models.CharField(max_length=200, blank=True, verbose_name="留言")
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")
    pay_type = models.SmallIntegerField(choices=PAY_TYPE, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    pay_sn = models.CharField(max_length=64, blank=True, verbose_name="支付编号")

    receive_person = models.CharField(max_length=20, verbose_name="收货人")
    receive_address = models.CharField(max_length=100, verbose_name="收货地址")
    receive_mobile = models.CharField(max_length=20, verbose_name="收货电话")

    logistics_status = models.SmallIntegerField(choices=LOGISTICS_STATUS, default=0, verbose_name="物流状态")

    total_amount = models.FloatField(default=0, verbose_name="总价")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
      verbose_name = "订单"
      verbose_name_plural = verbose_name

    def __str__(self):
      return str(self.id)


class OrderMerc(models.Model):
  order = models.ForeignKey(Order, verbose_name="所属订单")
  merchandise = models.ForeignKey(Merchandise, verbose_name="商品ID")
  num = models.IntegerField(verbose_name="数量")
  unit_price = models.FloatField(verbose_name="单价")
