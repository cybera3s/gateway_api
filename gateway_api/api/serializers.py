from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")

    def save(self, **kwargs):
        """
        overwrites save method to implement on the fly create and update
        """
        validated_data = {**self.validated_data, **kwargs}
        # updating
        if self.instance is not None:
            self.instance = User(**validated_data)

        return self.instance
