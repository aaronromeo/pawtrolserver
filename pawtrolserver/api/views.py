from rest_framework.views import APIView
from rest_framework.response import Response

from api.permissions import IsOwner


class LogoutView(APIView):
    permission_classes = (IsOwner,)

    def post(self, request, args, kwargs):
        pass
