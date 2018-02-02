from . import models

from django.db.models.query import Q

from django_filters.rest_framework import FilterSet
from django_filters import rest_framework as filters

class MerchandiseFilter(FilterSet):
  max_market_price = filters.NumberFilter(name="market_price", lookup_expr="lte")
  min_market_price = filters.NumberFilter(name="market_price", lookup_expr="gte")
  subclass = filters.NumberFilter(method="filter_subclass")

  def filter_subclass(self, queryset, name, value):
    return queryset.filter(Q(subclass_id=value)|Q(subclass__parent_class_id=value)|Q(subclass__parent_class__parent_class_id=value))

  class Meta:
    model = models.Merchandise
    fields = ["max_market_price", "min_market_price"]
