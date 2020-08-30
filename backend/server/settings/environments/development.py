from typing import List

from server.settings.components import BASE_DIR, config
from server.settings.components.common import INSTALLED_APPS
from server.settings.components.drf import REST_FRAMEWORK

DEBUG = True

ALLOWED_HOSTS = [
    config("ALLOWED_HOST"),
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "[::1]",
]

INSTALLED_APPS += ("drf_yasg",)

# Static files:
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS: List[str] = []

# DRF development settings
REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [
    "rest_framework.authentication.BasicAuthentication",
    "rest_framework.authentication.SessionAuthentication",
]

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += [  # type: ignore
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# Templates
# https://docs.djangoproject.com/en/2.2/ref/templates/api

TEMPLATES = [
    {
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # Contains plain text templates, like `robots.txt`:
            BASE_DIR.joinpath("server", "templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                # Default template context processors:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "debug": DEBUG,
        },
    },
]
