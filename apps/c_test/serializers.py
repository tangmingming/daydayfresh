
import sys
print(sys.path)
from rest_framework import serializers

from .models import Person
from . import models

class PersonSearialize(serializers.ModelSerializer):

    # code = serializers.CharField(max_length=10)

    class Meta:
        model = Person
        fields = "__all__"
        # exclude = ("code", )


class TestSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=4)



class CompanSerializer(serializers.ModelSerializer):
  persons = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model = models.Company
    fields = "__all__"
