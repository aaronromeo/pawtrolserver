from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthenticatedUser(BasePermission):
    """
    """
    def has_object_permission(self, request, view, obj):
        if not (request.user and request.user.is_authenticated()):
            return False
        return obj == request.user


class IsBusinessOwnerOrSafeMethods(BasePermission):
    """
    """
    def has_object_permission(self, request, view, obj):
        if not (request.user and request.user.is_authenticated()):
            return False
        elif request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user
