from __future__ import absolute_import
from .base import *

MEDIA_ROOT = PROJECT_DIR.parent.child('data')
STATIC_ROOT = PROJECT_DIR.child('static-root')

from bundle_config import config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%(host)s:%(port)s' % config['redis'],
        'OPTIONS': {
            'PASSWORD': config['redis']['password'],
        },
        'VERSION': config['core']['version'],
    },
}

