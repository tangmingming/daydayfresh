from django.shortcuts import render

from rest_framework.viewsets import ViewSet

# Create your views here.

class SmsViewSet(ViewSet):
    #check短信验证码
    def list(self, request):
        pass

    #发送短信验证码
    def create(self, request):
        pass
