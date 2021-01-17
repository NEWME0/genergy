from __future__ import absolute_import

from .base import *


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']


# Swagger settings
if 'drf_spectacular' in INSTALLED_APPS:
    pass


# Debug toolbar settings
if 'debug_toolbar' in INSTALLED_APPS:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
