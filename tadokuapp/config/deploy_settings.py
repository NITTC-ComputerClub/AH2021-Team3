import dj_database_url
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


db_from_env = dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config()
}
