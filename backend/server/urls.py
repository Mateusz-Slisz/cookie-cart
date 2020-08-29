from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from server.settings import DJANGO_ENV, DjangoSettingsVersion

urlpatterns = [
    path(f"{settings.ADMIN_PANEL_ROUTE}/", admin.site.urls),
]

if DJANGO_ENV == DjangoSettingsVersion.DEVELOPMENT:  # pragma: no cover
    from health_check import urls as health_urls
    from server.settings.swagger import schema_view

    urlpatterns += [
        # Health checks:
        path("health", include(health_urls)),
        # API Docs
        path(
            "swagger",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger",
        ),
    ]
