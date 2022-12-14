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
from django.contrib.auth.hashers import make_password

from grpc_utils.grpc_client import Client
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        Fetch and Managing Users
    """

    serializer_class = UserSerializer
    http_method_names = ["get", "post", "put", "delete"]
    grpc_client = Client()

    def get_queryset(self):
        return None

    def list(self, request, *args, **kwargs):
        """
            Get users list
        """

        try:
            serializer = self.get_serializer(self.grpc_client.get_users_list(), many=True)
        except Exception as e:
            return Response(e.details())

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
            Retrieve a User with provided ID
        """
        try:
            obj = self.grpc_client.get_user_by_id(int(kwargs.get('pk')))
        except Exception as e:
            return self.handle_error(e)

        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
            Creates a new user with provided payload fields
        """
        try:
            request.data['password'] = make_password(request.data['password'])
            new_user = self.grpc_client.create_new_user(User(**request.data))
        except Exception as e:
            return self.handle_error(e)

        serializer = self.get_serializer(new_user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
            Update an existing user with provided ID and payload fields
        """
        request.data['password'] = make_password(request.data['password'])
        instance = User(**request.data)

        try:
            updated_user = self.grpc_client.update_user(int(kwargs.get('pk')), instance)
        except Exception as e:
            return self.handle_error(e)

        serializer = self.get_serializer(updated_user)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
            Delete a user with provided User ID
        """
        try:
            self.grpc_client.delete_user_by_id(int(kwargs.get('pk')))
        except Exception as e:
            return self.handle_error(e)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def handle_error(err: Exception) -> Response:
        """
            get Exception object and returns response
            with Appropriate status code
        """

        # default status code 400
        status_code = status.HTTP_400_BAD_REQUEST

        if hasattr(err, 'code') and err.code() == StatusCode.NOT_FOUND:
            status_code = status.HTTP_404_NOT_FOUND
            response = err.details()
        else:
            response = str(err)

        return Response(response, status=status_code)
