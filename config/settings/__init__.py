import django_heroku
import dj_database_url

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['genergy-backend.herokuapp.com']
DATABASES['default'] = dj_database_url.config()

django_heroku.settings(locals())
