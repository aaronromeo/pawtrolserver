# from rest_framework import viewsets
# from profiles.models import User
# from profiles.serializers import UserSerializer


from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser, IsAuthorized
from rest_framework.views import APIView

from profiles.models import User
from profiles.permissions import IsObjOwner
from profiles.serializers import UserSerializer


# class OwnerDetailView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer

#     def get_object(self):
#         if not self.request.user:
#             raise Http404
#         obj = self.request.user
#         self.check_object_permissions(self.request, obj)
#         return obj


class OwnerListView(generics.ListCreateAPIView):
    # TODO: We need to determine scope of queryset
    # TODO: Determine correct permissions
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        if not self.request.user:
            raise Http404

        owners = User.objects.filter(ownerprofile__isnull=False)


class CurrentUserView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.

    """
    permission_classes = (IsObjOwner,)
    serializer_class = UserSerializer

    def get_object(self):
        if not self.request.user:
            raise Http404
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj

class UserDetailView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.

    Only intended for admins

    """
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class UserListView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be listed or created.

    Only intended for admins

    """
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
