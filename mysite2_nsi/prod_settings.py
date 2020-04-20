import dj_database_url
from .settings import *


DEBUG = True

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['morning-dusk-78597.herokuapp.com']


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'