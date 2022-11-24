from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Room
from .permissions import IsOwnerOrReadOnly
from .serializers import RoomSerializer, UserSerializer


class RoomViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
