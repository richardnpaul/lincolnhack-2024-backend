from stripes_with_pride.settings.base import * # noqa

ALLOWED_HOSTS = ['*']
DEBUG = True
SECRET_KEY = 'django-insecure-#1^'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "db",
        "NAME": "stripes_with_pride",
        "USER": "stripes_with_pride",
        "PASSWORD": "1MkKw3L3GJFsswVN2ADqRQqGWX6IgawuiKmTJyYAkY4R2g1ujN",
    }
}
