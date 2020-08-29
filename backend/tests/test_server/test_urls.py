import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == status.HTTP_200_OK


def test_admin_unauthorized(client):
    response = client.get(reverse("admin:index"))

    assert response.status_code == status.HTTP_302_FOUND


def test_admin_authorized(admin_client):
    response = admin_client.get(reverse("admin:index"))

    assert response.status_code == status.HTTP_200_OK


def test_documentation(client):
    """This test ensures that Swagger documentation is accessible."""
    response = client.get(reverse("schema-swagger"))

    assert response.status_code == status.HTTP_200_OK
