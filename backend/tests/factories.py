import factory.fuzzy

from server.apps.cart.models import Cart, Item


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart


class ItemFactory(factory.django.DjangoModelFactory):
    cart = factory.SubFactory(CartFactory)
    external_id = factory.Faker("uuid4")
    name = factory.Faker("word")
    value = factory.Faker("pyint", min_value=1)

    class Meta:
        model = Item
