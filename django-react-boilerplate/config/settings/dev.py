import json

from .base import *

if SERVER_ENV == "Local":
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')


    def custom_show_toolbar(self):
        return True


    DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar}

INTERNAL_IPS = ["127.0.0.1"]

# Database 설정
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = env_json['DATABASES']

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
]
