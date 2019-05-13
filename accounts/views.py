from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import CustomUser

from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import (
    UserListSerializer,
    UserCreateSerializer
)


class UserListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer


class UserCreate(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
