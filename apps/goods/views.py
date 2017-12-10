from .serializers import MerchandiseSerializer
from .models import Merchandise

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from rest_framework import mixins
from rest_framework import permissions

from . import models
from . import serializers

# Create your views here.

class Classification(viewsets.ModelViewSet):
    queryset = models.Classification.objects.all()
    serializer_class = serializers.ClassificationSerializer


class Merchandise(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

