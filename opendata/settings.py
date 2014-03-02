"""
Django settings for opendata project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=dz6@%2bju16vm=8$v-$mrmu19n&-w2#r8)ih$9@ug%4o07h=0y-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False   # turn off once I push to AWS
TEMPLATE_DEBUG = False # ^^

# When you go to proudction you need to add the host once DEBUG is set to false
ALLOWED_HOSTS = [
	'.jarenglover.com' # in Production django restricts the host that can access your app 
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fuel',
    'tastypie',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware', #next three lines where added for redis    # This middleware must be first on the list
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'opendata.urls'

WSGI_APPLICATION = 'opendata.wsgi.application'

# CACHE  - Redis socket

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '/var/run/redis/redis.sock',
    },
}

# config redis as the session engine 

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = { 
 
 
 
    'default': { 
 
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'. 
 
            'NAME': 'fuel',                      # Or path to database file if using sqlite3. 
 
            # The following settings are not used with sqlite3: 
 
            'USER': 'illwill', 
 
            'PASSWORD': '1D@t@$0ur30fGr3@tn3$$4', 
 
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP. 
 
            'PORT': '5432',                      # Set to empty string for default. 
 
        } 
} 

'''DATABASES = {

    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '',                      # Or path to database file if using sqlite3.
            					# The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',                      # Set to empty string for default.
        }
}'''


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Tastypie Setting
API_LIMIT_PER_PAGE = 35 # I wanted to change the defult limit this instead of 20
TASTYPIE_DEFAULT_FORMATS = ['json'] # force to default to json ...
