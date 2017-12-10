from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Merchandise

# Create your models here.

User = get_user_model()

class RecevingAddress(models.Model):
    """
    收货地址
    """
    desc = models.CharField(max_length=30, default="", blank=True, verbose_name="说明")

    User = models.ForeignKey(User, verbose_name="用户")
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    address = models.CharField(max_length=100, verbose_name="地址")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


class Collect(models.Model):
    """
    收藏
    """
    user = models.ForeignKey(User, verbose_name="用户")
    merchandise = models.ForeignKey(Merchandise, verbose_name="商品")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


class Message(models.Model):
    """
    用户留言
    """

    MSG_TYPE = (
        (0, "留言"),
        (1, "投诉"),
        (2, "咨询"),
        (3, "售后"),
        (3, "求购"),
        (10, "其它"),
    )

    user = models.ForeignKey(User, verbose_name="用户")
    msg_type = models.SmallIntegerField(choices=MSG_TYPE, verbose_name="留言类型")
    subject = models.CharField(max_length=30, verbose_name="主题")
    msg = models.TextField(default="", blank=True, verbose_name="留言内容")
    file = models.FileField(null=True, verbose_name="文件")

class Revert(models.Model):
    message = models.ForeignKey(Message, verbose_name="留言")
    user = models.ForeignKey(User, verbose_name="用户")
    msg = models.TextField(verbose_name="内容")
    file = models.FileField(null=True, verbose_name="文件")