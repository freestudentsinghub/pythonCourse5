from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from habits.models import Habits
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import send_telegram_message


# Create your views here.

class PublicListAPIView(generics.ListAPIView):
    """Вывод публичных привычек."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = HabitPaginator


class HabitListAPIView(generics.ListAPIView):
    """Просмотр привычек пользователя."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitPaginator

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

    def perform_create(self, serializer):
        """Создаем привычку и отправляем сообщение пользователю в Телеграм."""
        habit = serializer.save()
        habit.user = self.request.user
        habit = serializer.save()
        habit.save()
        if habit.user.tg_chat_id:
            send_telegram_message(habit.user.tg_chat_id, "Создана новая привычка!")


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки."""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки."""
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)