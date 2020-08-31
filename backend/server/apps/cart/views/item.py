from typing import Any, Optional

from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from server.apps.cart.constants import CART_ID_COOKIE_KEY
from server.apps.cart.entities.item import ItemEntity
from server.apps.cart.models import Item
from server.apps.cart.serializers import ItemInputSerializer
from server.apps.cart.services.cart import set_cart_id_cookie
from server.apps.cart.services.item import create_or_update_item_in_cart


class ItemCreateAPIView(views.APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=ItemInputSerializer,
        response={status.HTTP_204_NO_CONTENT: ""},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = ItemInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response(status=status.HTTP_204_NO_CONTENT)

        item_entity: ItemEntity = ItemEntity(**serializer.validated_data)
        cart_id_cookie: Optional[str] = request.COOKIES.get(CART_ID_COOKIE_KEY)

        item: Item = create_or_update_item_in_cart(
            item_entity=item_entity, cart_id=cart_id_cookie,
        )
        set_cart_id_cookie(
            response=response,
            cart_id=str(item.cart_id),
            cart_id_cookie=cart_id_cookie,
        )

        return response
