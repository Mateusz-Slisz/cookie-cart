import pytest
from django.contrib.auth.models import User
from django.test import Client
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(
        username="admin", email="", password="password"
    )


@pytest.fixture
def admin_client(admin_user):
    client = Client()
    client.login(username=admin_user.username, password="password")

    return client
