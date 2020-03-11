import dj_database_url
import django_heroku

from .base import *

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {'default': dj_database_url.config(
    conn_max_age=600, ssl_require=True)}

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


servers = config('MEMCACHIER_SERVERS')
username = config('MEMCACHIER_USERNAME')
password = config('MEMCACHIER_PASSWORD')
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,
        'LOCATION': servers,
        'OPTIONS': {
            'binary': True,
            'username': username,
            'password': password,
            'behaviors': {
                # Enable faster IO
                'no_block': True,
                'tcp_nodelay': True,
                # Keep connection alive
                'tcp_keepalive': True,
                # Timeout settings
                'connect_timeout': 2000,  # ms
                'send_timeout': 750 * 1000,  # us
                'receive_timeout': 750 * 1000,  # us
                '_poll_timeout': 2000,  # ms
                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30,
            }
        }
    }
}


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
