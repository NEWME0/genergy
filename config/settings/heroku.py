import django_heroku
import dj_database_url

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['genergy-backend.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())
