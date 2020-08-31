import uuid

from django.core.validators import MinValueValidator
from django.db import models

from server.apps.cart.models.cart import Cart


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=255)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items",
    )
    name = models.CharField(max_length=255, blank=True)
    value = models.PositiveSmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(1)],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("cart", "external_id"), name="unique_item_in_cart",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.external_id} in {self.cart_id}"
