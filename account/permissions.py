import re
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrAccountant(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True         


class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True         


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True         
