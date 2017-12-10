from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Merchandise
# Create your models here.

User = get_user_model()

class ShoppingCard(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name="用户")
    total_amount = models.FloatField(default=0, verbose_name="金额")
    total_num = models.ImageField(default=0, verbose_name="总数量")

class ShopCardMerc(models.Model):
    """
    购物车商品
    """

    shoping_card = models.ForeignKey(ShoppingCard, verbose_name="购物车")
    merchandise = models.ForeignKey(Merchandise, verbose_name="商品")
    num = models.IntegerField(verbose_name="数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


class Order(models.Model):
    """
    订单
    """
    STATUS = (
        (0, "未支付"),
        (1, "已支付"),
        (2, "已取消"),
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
    sn = models.CharField(max_length=50, unique=True, verbose_name="订单编号")
    status = models.SmallIntegerField(choices=STATUS, verbose_name="订单状态")
    message = models.CharField(max_length=200, blank=True, verbose_name="留言")
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")
    pay_type = models.SmallIntegerField(choices=PAY_TYPE, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    pay_sn = models.CharField(max_length=50, verbose_name="支付编号")

    receive_person = models.CharField(max_length=20, verbose_name="收货人")
    receive_address = models.CharField(max_length=100, verbose_name="收货地址")
    receive_mobile = models.CharField(max_length=10, verbose_name="收货电话")

    logistics_status = models.SmallIntegerField(choices=LOGISTICS_STATUS, verbose_name="物流状态")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")


class OrderMerc(models.Model):
    """
    购物车商品
    """

    order = models.ForeignKey(ShoppingCard, verbose_name="购物车")
    merchandise = models.ForeignKey(Merchandise, verbose_name="商品")
    num = models.IntegerField(verbose_name="数量")