"""

Test-only Django settings for the dh@mit computational history project.

DO NOT run with this file in production

"""

from .settings import *

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'comphist',
        'USER': 'postgres',
    }
}
