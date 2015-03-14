from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated()):
            return True
        return False
