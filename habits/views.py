from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from habits.models import Habits
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


# Create your views here.

class PublicListAPIView(generics.ListAPIView):
    """Вывод публичных привычек."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = (AllowAny,)


class HabitListAPIView(generics.ListAPIView):
    """Просмотр привычек пользователя."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр подробностей привычки."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)