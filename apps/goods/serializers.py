from .models import Merchandise

from rest_framework import serializers

from . import models

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classification
        fields = "__all__"

class MerchandiseSerializer(serializers.ModelSerializer):
    subclass = ClassificationSerializer(required=False)
    class Meta:
        model = Merchandise
        fields = "__all__"