from django.urls import include, path

from server.settings import DJANGO_ENV, DjangoSettings

urlpatterns = [path("", include("server.apps.cart.urls"))]

if DJANGO_ENV == DjangoSettings.development.value:  # pragma: no cover
    # drf-auth
    urlpatterns += [
        path("", include("rest_framework.urls", namespace="rest_framework")),
    ]
