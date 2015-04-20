from rest_framework.permissions import BasePermission


class IsObjOwner(BasePermission):
    """
    """
    def has_object_permission(self, request, view, obj):
        if not (request.user and request.user.is_authenticated()):
            return False
        return obj == request.user
