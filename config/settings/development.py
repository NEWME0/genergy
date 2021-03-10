from . import *

DEBUG = True

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BaseAuthentication',
)

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
