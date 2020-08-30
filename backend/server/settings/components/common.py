from typing import Tuple

from server.settings.components import config

SECRET_KEY = config("DJANGO_SECRET_KEY")

# Application definition:
INSTALLED_APPS: Tuple[str, ...] = (
    # Default django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # django-admin:
    "django.contrib.admin",
    # Your apps go here:
    # Health checks:
    "health_check",
    "health_check.db",
    # Third part apps
    "django_extensions",
)


MIDDLEWARE: Tuple[str, ...] = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "server.urls"

WSGI_APPLICATION = "server.wsgi.application"

# Disables redirecting to the same URL with a slash at the end
APPEND_SLASH = False

# Routes
ADMIN_PANEL_ROUTE = config("ADMIN_PANEL_ROUTE")

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("DJANGO_DATABASE_HOST"),
        "PORT": config("DJANGO_DATABASE_PORT", cast=int),
        "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=60),
        "OPTIONS": {"connect_timeout": 10},
    },
}


# Internationalization
LANGUAGE_CODE = "en-us"

USE_I18N = False
USE_L10N = False

USE_TZ = True
TIME_ZONE = "UTC"


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/api/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# Django authentication system
# https://docs.djangoproject.com/en/2.2/topics/auth/

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
]
