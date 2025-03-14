from django.urls import path

from habits.views import (HabitCreateAPIView, HabitDestroyAPIView,
                          HabitListAPIView, HabitRetrieveAPIView,
                          HabitUpdateAPIView, PublicListAPIView)

app_name = 'habits'

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habits"),
    path("public/", PublicListAPIView.as_view(), name="public_habits"),
    path("create/", HabitCreateAPIView.as_view(), name="create_habits"),
    path("retrieve/<int:pk>/", HabitRetrieveAPIView.as_view(), name="retrieve_habits"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="update_habits"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="delete_habits"),
]