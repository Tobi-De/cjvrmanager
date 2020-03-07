import dj_database_url
import django_heroku

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
