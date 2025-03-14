from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@sky.com', password='123456')

    def test_user_create(self):
        self.assertEqual(CustomUser.objects.all().count(), 1)