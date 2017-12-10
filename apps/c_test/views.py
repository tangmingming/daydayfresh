import datetime

from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets

from . import serializers
from . import models

class Index(generics.ListAPIView):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSearialize


class Test_1(APIView):
    def get(self, request, *args, **kwargs):
        print(__name__)
        return Response(datetime.datetime.now())


class Test_2(generics.CreateAPIView):
    serializer_class = serializers.PersonSearialize


# class PersonViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.PersonSearialize
#     queryset = models.Person.objects.all()

# class PersonViewSet(viewsets.ViewSet):
#     def list(self, request):
#         print("body:")
#         print(request.body)
#         return Response("list")
#
#     def create(self, request):
#         return Response("create")
#
#     def retrieve(self, request, pk=None):
#         return Response("retireve")
#
#     def update(self, request, pk=None):
#         return Response("update")
#
#     def partial_update(self, request, pk=None):
#         return Response("partial_update")
#
#     def destroy(self, request, pk=None):
#         return Response("destroy")

class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSearialize

    def list(self, request, *args, **kwargs):
        queryset = models.Person.objects.all()
        serializer = serializers.Person()

class TestViewSet(viewsets.ViewSet):
    pass