from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
        Managing Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    
   
    def perform_destroy(self, instance):
        """
            do not delete instance from database just return False
        """
        return False
    