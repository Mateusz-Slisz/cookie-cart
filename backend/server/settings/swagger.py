from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Cookie cart",
        default_version="v1",
        description="Simple app for adding items to cookie cart",
        contact=openapi.Contact(email="mat.slisz@yahoo.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
