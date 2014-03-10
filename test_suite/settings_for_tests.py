import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'LkfBr693tY3b2wL9a8XR8rrQmDxRKzPyPcQZ2Tz5JHKNaKEe'

USE_I18N = True
LANGUAGE_CODE = 'en'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
