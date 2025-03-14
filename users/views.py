from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializer import CustomUserSerializer


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
