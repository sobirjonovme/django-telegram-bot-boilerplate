from .base import *  # noqa

STAGE = "develop"
DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True

# default sqlite database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

