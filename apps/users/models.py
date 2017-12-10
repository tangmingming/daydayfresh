from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ShopUser(AbstractUser):
    """
    用户模型
    """
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name="昵称")
    mobile = models.CharField(max_length=11, unique=True,   verbose_name="手机号码")
    # password = models.CharField(max_length=100, verbose_name="密码")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    reg_time = models.DateTimeField(default=datetime.now, verbose_name="注册时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.nickname, self.mobile)

class VerifyCode(models.Model):
    """
    短信验证码模型
    """
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    code = models.CharField(max_length=10, verbose_name="短信验证码")
    send_time = models.DateTimeField(auto_now_add=True, verbose_name="发送时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.mobile, self.code)