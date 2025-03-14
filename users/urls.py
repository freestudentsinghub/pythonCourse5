from rest_framework.permissions import AllowAny
from django.urls import path

from users.views import UserCreateAPIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

app_name = "users"


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]