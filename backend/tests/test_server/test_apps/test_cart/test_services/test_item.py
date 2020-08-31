import uuid
from dataclasses import asdict

import pytest

from server.apps.cart.entities.item import ItemEntity
from server.apps.cart.models import Item, Cart
from server.apps.cart.services.item import create_or_update_item_in_cart
from tests.factories import CartFactory, ItemFactory


@pytest.fixture
def item_entity() -> ItemEntity:
    return ItemEntity(external_id="EX123", name="hello0captain", value=100)


@pytest.mark.parametrize(
    "invalid_cart_id", [None, "not_uuid_format", str(uuid.uuid4())]
)
@pytest.mark.django_db
def test_create_or_update_item_in_cart_creates_item_and_cart(
    item_entity, invalid_cart_id
):
    """
    Function creates new item along with cart,
    when `cart_id` is not given, has wrong format or does not exist
    """
    item: Item = create_or_update_item_in_cart(
        item_entity=item_entity, cart_id=invalid_cart_id
    )

    # ensures that cart and item are created with correct values
    assert Cart.objects.filter(items=item).exists()
    assert Item.objects.filter(
        pk=item.pk, cart=item.cart, **asdict(item_entity)
    ).exists()


@pytest.mark.django_db
def test_create_or_update_item_in_cart_creates_item_in_cart(item_entity):
    """Function creates item in existing cart, when `cart_id` exists"""
    cart = CartFactory.create()
    ItemFactory.create(cart=cart)

    item: Item = create_or_update_item_in_cart(
        item_entity=item_entity, cart_id=cart.pk
    )

    # ensures that item is created with correct values
    assert cart.items.count() == 2
    assert Item.objects.filter(
        pk=item.pk, cart=cart, **asdict(item_entity)
    ).exists()


@pytest.mark.django_db
def test_create_or_update_item_in_cart_updates_item_in_cart(item_entity):
    """
    Function updates existing item in cart,
    when `cart_id` exists and item has same `external_id`
    """
    cart = CartFactory.create()
    ItemFactory.create(external_id=item_entity.external_id, cart=cart)

    item: Item = create_or_update_item_in_cart(
        item_entity=item_entity, cart_id=cart.pk
    )

    # ensures that item is updated with correct values
    assert cart.items.count() == 1
    assert Item.objects.filter(
        pk=item.pk, cart=cart, **asdict(item_entity)
    ).exists()
