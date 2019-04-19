"""

Test-only Django settings for the dh@mit computational history project.

DO NOT run with this file in production

"""

from .settings import *

# Database

# NOTE(ra): This lets us run our tests on sqlite3, which is ultimately
# not a very good idea -- but works around the fact that our postgres user is readonly.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    },
}
