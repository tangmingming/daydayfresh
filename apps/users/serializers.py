import re

from django.conf import settings
from rest_framework import serializers

from users import models

class VerifyCodeSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.VerifyCode
        fields = ("mobile", "code")

    def validate_mobile(self, value):
        if not re.match(settings.REGEX_MOBILE, value):
            raise serializers.ValidationError("手机号不正确")
        return value

    def validate_code(self, value):
        print(settings.REGEX_VERIFYCODE)
        ret = re.match(settings.REGEX_VERIFYCODE, value)
        print(ret)
        if None==re.match(settings.REGEX_VERIFYCODE, value):
            raise serializers.ValidationError("验证码错误")
        return value

class ShopUserSerialize(serializers.ModelSerializer):

    # code = serializers.CharField(max_length=10)

    # INVIDITY_PERIOD = settings.SMS["validity_period"]
    # def validate_code(self, value):
    #     if not re.match(settings.SMS["regex_verifycode"], value):
    #         raise serializers.ValidationError("验证码格式错误")
    #     return value

    def validate_password(self, value):
        if(len(value)<6 or len(value)>15):
            return serializers.ValidationError("密码长度必须大于6小于15")
        return value

    def create(self, validated_data):
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