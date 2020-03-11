from .base import *

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['testserver', 'localhost']

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = [
    '127.0.0.1',
]
