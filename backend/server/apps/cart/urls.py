from django.urls import path

from server.apps.cart.views import ItemCreateAPIView

app_name = "cart"

urlpatterns = [path("item", ItemCreateAPIView.as_view(), name="item-create")]
