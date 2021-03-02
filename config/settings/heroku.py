import django_heroku
import dj_database_url

from . import *

DEBUG = True

ALLOWED_HOSTS = ['genergy-backend.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

django_heroku.settings(locals())
