from rest_framework import viewsets
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.validators import ValidationError
from rest_framework import status
import json
from grpc import StatusCode

from grpc_utils.grpc_client import Client
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        Fetch and Managing Users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post", "put", "delete"]
    grpc_client = Client()

    def list(self, request, *args, **kwargs):
        """
            Get users list
        """

        try:
            serializer = self.get_serializer(self.grpc_client.get_users_list(), many=True)
        except Exception as e:
            return Response(e.details())

        return Response(serializer.data)


