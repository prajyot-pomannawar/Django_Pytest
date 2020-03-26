import pytest
import json
from rest_framework import status
from django.test import TestCase, Client, client
from django.urls import reverse
from ..models import User
from ..serializer import UserSerializer


@pytest.mark.django_db
class TestView:
    def test_view_user(self, client):
        """
        Method for displaying all users from the database
        """
        response = client.get('/users')
        user_list = User.objects.all()
        serializer = UserSerializer(user_list, many=True)
        assert response.data == serializer.data
        assert response.status_code == status.HTTP_200_OK
