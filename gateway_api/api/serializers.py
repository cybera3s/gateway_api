from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
    def save(self, **kwargs):
        """
        overwrites save method to implement on the fly create and update
        """
        return self.instance