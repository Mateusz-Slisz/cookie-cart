from dataclasses import asdict
from typing import Optional

from django.core import exceptions as django_exceptions
from django.db import transaction

from server.apps.cart.entities import ItemEntity
from server.apps.cart.models import Item, Cart


def create_or_update_item_in_cart(
    *, item_entity: ItemEntity, cart_id: Optional[str],
) -> Item:
    try:
        cart = Cart.objects.get(pk=cart_id)
        item, _ = Item.objects.update_or_create(
            external_id=item_entity.external_id,
            cart=cart,
            defaults={"name": item_entity.name, "value": item_entity.value},
        )
    except (Cart.DoesNotExist, django_exceptions.ValidationError):
        with transaction.atomic():
            item = Item.objects.create(
                cart=Cart.objects.create(), **asdict(item_entity),
            )

    return item
