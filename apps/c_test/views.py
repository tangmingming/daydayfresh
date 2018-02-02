import datetime

from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

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
  filter_backends = (DjangoFilterBackend, )
  filter_fields = "__all__"
  # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

# a = PersonViewSet()
# a.get_serializer(data="aaa")
# a.as_view()

class CompanyViewSet(viewsets.ModelViewSet):
  queryset = models.Company.objects.all()
  serializer_class = serializers.CompanSerializer
  filter_backends = (DjangoFilterBackend, )
  filter_fields = "__all__"
