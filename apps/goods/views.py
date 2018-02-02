from .serializers import MerchandiseSerializer
from .models import Merchandise

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
import django_filters
from rest_framework.filters import SearchFilter, OrderingFilter
from utils.paging import PageSizeNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import permissions

from django_filters import rest_framework as filters

from . import models
from . import serializers
from . import filter as local_filters

# Create your views here.

class Classification(viewsets.ModelViewSet):
    queryset = models.Classification.objects.all()
    serializer_class = serializers.ClassificationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ("c_type", )
    search_fields = ("name", "desc", "=code")
    ordering_fields = ("id", "name", "c_type")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(c_type=1))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Merchandise(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer
    def aa(self):
      self.get_queryset()

class MerchandiseViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
  queryset = models.Merchandise.objects.all()
  serializer_class = MerchandiseSerializer
  pagination_class = PageSizeNumberPagination
  filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
  filter_class = local_filters.MerchandiseFilter
  ordering = ("-add_time", )
  ordering_fields = ("sales_numm", "sale_price")
  search_fields = ("name", )
