from rest_framework.permissions import BasePermission, SAFE_METHODS

from users import models

class GetUserInfoPermisson(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in ["HEAD", "OPTIONS", "POST"] or request.user.is_staff:
      return True

    return obj.id == request.user.id

class GetGoodCardPermission(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in ["HEAD", "OPTIONS", "POST"] or request.user.is_staff:
      return True

    return obj.user.id == request.user.id

class GetOrderPermission(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in ["HEAD", "OPTIONS", "POST"] or request.user.is_staff:
      return True

    return obj.user.id == request.user.id


class GetUpdatePermission(BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in ["HEAD", "OPTIONS", "POST"] or request.user.is_staff:
      return True

    return obj.user == request.user

