# from rest_framework import viewsets
# from profiles.models import User
# from profiles.serializers import UserSerializer


from django.http import Http404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from profiles.models import User
from profiles.serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class OwnerDetailView(generics.ListCreateAPIView):
#     queryset = User.objects.filter(ownerprofile__isnull=False)
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         user = self.request.user
#         User.objects.filter(ownerprofile__isnull=False)


class OwnerListView(generics.ListCreateAPIView):
    queryset = User.objects.filter(ownerprofile__isnull=False)
    serializer_class = UserSerializer


class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=data) #, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
