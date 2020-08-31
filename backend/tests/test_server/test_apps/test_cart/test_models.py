from tests.factories import CartFactory, ItemFactory


def test_cart_model_string_representation():
    cart = CartFactory.build()

    assert str(cart) == f"{cart.pk}"


def test_item_model_string_representation():
    cart = CartFactory.build()
    item = ItemFactory.build(cart=cart)

    assert str(item) == f"{item.external_id} in {cart.pk}"
