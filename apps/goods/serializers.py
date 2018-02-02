from .models import Merchandise

from rest_framework import serializers

from . import models

class ClassificationSerializer3(serializers.ModelSerializer):
    class Meta:
        model = models.Classification
        fields = "__all__"

class ClassificationSerializer2(serializers.ModelSerializer):
    childs = ClassificationSerializer3(many=True, read_only=True)
    class Meta:
        model = models.Classification
        fields = "__all__"

class ClassificationSerializer(serializers.ModelSerializer):
    childs = ClassificationSerializer2(many=True, read_only=True)
    class Meta:
        model = models.Classification
        fields = "__all__"

class MerchandiseSerializer(serializers.ModelSerializer):
    # subclass = ClassificationSerializer(required=False)
    class Meta:
        model = Merchandise
        fields = "__all__"
