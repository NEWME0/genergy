import django_heroku

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['genergy-backend.herokuapp.com']

django_heroku.settings(locals())
