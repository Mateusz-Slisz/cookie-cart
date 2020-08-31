from typing import Optional

from server.apps.cart.constants import (
    CART_ID_COOKIE_KEY,
    CART_ID_COOKIE_AGE,
)
from server.apps.cart.types import ResponseType


def set_cart_id_cookie(
    *, response: ResponseType, cart_id: str, cart_id_cookie: Optional[str],
) -> None:
    if cart_id_cookie is None or cart_id != cart_id_cookie:
        response.set_cookie(
            key=CART_ID_COOKIE_KEY, value=cart_id, max_age=CART_ID_COOKIE_AGE,
        )
