import uuid
from typing import Dict, Union

import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from server.apps.cart.constants import CART_ID_COOKIE_KEY, CART_ID_COOKIE_AGE
from server.apps.cart.models import Item, Cart


@pytest.fixture
def item_data() -> Dict[str, Union[str, int]]:
    return {"external_id": str(uuid.uuid4()), "name": "example", "value": 99}


@pytest.mark.django_db
def test_item_create_view_as_unauthorized_user(api_client, item_data):
    """Unauthorized user may create item"""
    response = api_client.post(reverse("cart:item-create"), data=item_data)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Item.objects.filter(**item_data).exists()


@pytest.mark.django_db
def test_item_create_view_sets_cart_id_cookie(api_client, item_data):
    """`cart_id` cookie is correctly set"""
    response = api_client.post(reverse("cart:item-create"), data=item_data)
    cart_id_cookie = response.cookies[CART_ID_COOKIE_KEY]

    assert Cart.objects.filter(pk=cart_id_cookie.value).count() == 1
    assert cart_id_cookie["max-age"] == CART_ID_COOKIE_AGE


@pytest.mark.django_db
def test_item_create_view_two_same_items(api_client, item_data):
    """First item is updated, when second has the same `external_id`"""
    api_client.post(reverse("cart:item-create"), data=item_data)
    api_client.post(reverse("cart:item-create"), data=item_data)

    assert Cart.objects.count() == 1
    assert Item.objects.count() == 1


@pytest.mark.django_db
def test_item_create_view_two_different_items(api_client, item_data):
    """All items are created, when `external_id` is different"""
    api_client.post(reverse("cart:item-create"), data=item_data)
    api_client.post(
        reverse("cart:item-create"), data={"external_id": str(uuid.uuid4())}
    )

    assert Cart.objects.count() == 1
    assert Item.objects.count() == 2
