from typing import Optional

from server.apps.cart.constants import (
    CART_ID_COOKIE_KEY,
    CART_ID_COOKIE_AGE,
)
from server.apps.cart.types import ResponseType


def set_cart_id_cookie(
    *, response: ResponseType, cart_id: str, cookie_cart_id: Optional[str],
) -> None:
    if cookie_cart_id is None or cart_id != cookie_cart_id:
        response.set_cookie(
            key=CART_ID_COOKIE_KEY, value=cart_id, max_age=CART_ID_COOKIE_AGE,
        )
