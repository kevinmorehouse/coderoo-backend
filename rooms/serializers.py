from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "owner",
            "created_at",
        )
        model = Room


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )
