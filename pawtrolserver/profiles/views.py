from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from profiles.models import User, ServiceBusiness
from profiles.permissions import IsAuthenticatedUser, IsBusinessOwnerOrSafeMethods
from profiles.serializers import UserSerializer, ServiceBusinessSerializer, WalkerProfileSerializer


# class OwnerDetailView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer

#     def get_object(self):
#         if not self.request.user:
#             raise Http404
#         obj = self.request.user
#         self.check_object_permissions(self.request, obj)
#         return obj


class OwnerListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        if not self.request.user:
            raise Http404

        owners = User.objects.filter(ownerprofile__isnull=False)

        return owners


class WalkerListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        if not self.request.user:
            raise Http404

        owners = User.objects.filter(walkerprofile__isnull=False)

        return owners


class CurrentUserView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.

    """
    permission_classes = (IsAuthenticatedUser,)
    serializer_class = UserSerializer

    def get_object(self):
        if not self.request.user:
            raise Http404
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj


class ServiceBusinessListView(generics.ListCreateAPIView):
    """
    API endpoint that allows a business to be viewed or edited.

    """
    permission_classes = (IsBusinessOwnerOrSafeMethods,)
    serializer_class = ServiceBusinessSerializer

    def get_queryset(self):
        if not self.request.user:
            raise Http404

        if self.request.user.is_staff:
            businesses = ServiceBusiness.objects.filter()
        elif hasattr(self.request.user, 'walkerprofile'):
            businesses = self.request.user.walkerprofile.businesses.all()

        return businesses


class ServiceBusinessDetailView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows a business to be viewed or edited.

    """
    permission_classes = (IsBusinessOwnerOrSafeMethods,)
    serializer_class = ServiceBusinessSerializer
    queryset = ServiceBusiness.objects.all()
    lookup_field = 'uuid'


class ServiceBusinessWalkerListView(generics.ListCreateAPIView):
    """
    API endpoint that allows the walkers of a business to be viewed or edited.

    """
    permission_classes = (IsBusinessOwnerOrSafeMethods,)
    serializer_class = WalkerProfileSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        business_uuid = self.kwargs['business_uuid']
        return ServiceBusiness.objects.get(uuid=business_uuid).walkerprofile_set.all()

    # def get_object(self):
    #     if not self.request.user:
    #         raise Http404
    #     obj = get_object_or_404(self.get_queryset())
    #     self.check_object_permissions(self.request, obj)
    #     return obj


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
