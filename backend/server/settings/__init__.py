from os import environ

from split_settings.tools import include


class DjangoSettingsVersion:
    DEVELOPMENT = "development"


DJANGO_ENV = environ.get("DJANGO_ENV", DjangoSettingsVersion.DEVELOPMENT)

base_settings = [
    "components/common.py",
    "components/drf.py",
    # For purpose of simplicity there is only development environment
    "environments/{django_env}.py".format(django_env=DJANGO_ENV),
]

# Include settings:
include(*base_settings)
