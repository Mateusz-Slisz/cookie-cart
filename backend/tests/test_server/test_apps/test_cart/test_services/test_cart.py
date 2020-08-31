import pytest
from rest_framework.response import Response

from server.apps.cart.constants import (
    CART_ID_COOKIE_KEY,
    CART_ID_COOKIE_AGE,
)
from server.apps.cart.services.cart import set_cart_id_cookie
from tests.factories import CartFactory


@pytest.fixture
def clean_response() -> Response:
    return Response()


@pytest.mark.django_db
def test_set_cart_id_cookie_sets_cart_cookie_when_cookie_does_not_exist(
    clean_response,
):
    """
    Function sets `cart_id` cookie to response with correct values,
    when `cart_id_cookie` does not exist
    """
    cart = CartFactory.create()

    set_cart_id_cookie(
        response=clean_response, cart_id=cart.pk, cart_id_cookie=None
    )
    cart_id_cookie = clean_response.cookies[CART_ID_COOKIE_KEY]

    assert cart_id_cookie.value == str(cart.pk)
    assert cart_id_cookie["max-age"] == CART_ID_COOKIE_AGE


@pytest.mark.django_db
def test_set_cart_id_cookie_sets_cart_cookie_when_cookie_is_invalid(
    clean_response, random_id
):
    """
    Function sets `cart_id` cookie to response with correct values,
    when `cart_id_cookie` is not same as `cart_id`
    """
    cart = CartFactory.create()

    set_cart_id_cookie(
        response=clean_response, cart_id=cart.pk, cart_id_cookie=random_id
    )
    cart_id_cookie = clean_response.cookies[CART_ID_COOKIE_KEY]

    assert cart_id_cookie.value == str(cart.pk)
    assert cart_id_cookie["max-age"] == CART_ID_COOKIE_AGE


@pytest.mark.django_db
def test_set_cart_id_cookie_does_nothing_when_cookie_is_valid(clean_response):
    """Function does nothing when `cart_id_cookie` is same as `cart_id`"""
    cart = CartFactory.create()

    set_cart_id_cookie(
        response=clean_response, cart_id=cart.pk, cart_id_cookie=cart.pk
    )

    assert CART_ID_COOKIE_KEY not in clean_response.cookies
