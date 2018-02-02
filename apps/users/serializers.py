import re
from datetime import datetime, timedelta

from django.conf import settings
from rest_framework import serializers

from users import models

class VerifyCodeSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.VerifyCode
        fields = ("mobile", )

    # def validate(self, attrs):
    #     print("validate:{}".format(attrs))
    #     print(attrs["mobile"])
    #     raise serializers.ValidationError("validate error")
    #     return attrs

    def validate_mobile(self, value):
        print("validate_mobile:{}".format(value))

        if not re.match(settings.REGEX_MOBILE, value):
            raise serializers.ValidationError("手机号不正确")
        if models.ShopUser.objects.filter(mobile=value):
            raise serializers.ValidationError("手机号已注册")
        return value

    # def validate_code(self, value):
    #     print("validate_code:{}".format(value))
    #     ret = re.match(settings.REGEX_VERIFYCODE, value)
    #     if None==re.match(settings.REGEX_VERIFYCODE, value):
    #         raise serializers.ValidationError("验证码错误")
    #     return value

class ShopUserSerialize(serializers.ModelSerializer):

    code = serializers.CharField(required=True, write_only=True, max_length=settings.SMS["verifycode_len"], min_length=settings.SMS["verifycode_len"],label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码")

    def validate(self, attrs):
        print("attrs:\n{}".format(attrs))
        return attrs

    def validated_email(self, value):
        print("validate_email:\n{}".format(value))
        return value

    def validate_code(self, value):
        print("validate_code:\n{}".format(value))
        ret = re.match(settings.REGEX_VERIFYCODE, value)
        if None==re.match(settings.REGEX_VERIFYCODE, value):
            raise serializers.ValidationError("验证码错误")
        query_sets = models.VerifyCode.objects.filter(mobile=value, send_time__gte=datetime.now()-timedelta(minutes=settings.SMS["validity_period"]))
        if not len(query_sets):
            return serializers.ValidationError("手机没有发送验证码记录")
        is_right = False
        for i in query_sets:
            if value == i.code:
                is_right = True
                break

        if not is_right:
            return serializers.ValidationError("验证码错误")

    def validate_password(self, value):
        if(len(value)<6 or len(value)>15):
            return serializers.ValidationError("密码长度必须大于6小于15")
        return value

    def validate_username(self, value):
        if(re.match("^\d+$", value)):
          return serializers.ValidationError("用户名不能为纯数字")
        return value

    def create(self, validated_data):
        validated_data.pop("code")
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = models.ShopUser
        fields = "__all__"
        # exclude = ("code", )
        extra_kwargs = {'password': {'write_only': True},
                        }
        # read_only_fields = ("password", )

class ReceInfoSerialize(serializers.ModelSerializer):
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())

  def validate(self, attrs):
    if self.Meta.model.objects.filter(user=self.context["request"].user).count() > 20:
      raise serializers.ValidationError("收货信息不能超过20个，请删除不常用后重试")
    return attrs
  class Meta:
    model = models.ReceInfo
    exclude = ("user", )
