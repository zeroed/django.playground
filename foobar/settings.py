"""
Django settings for foobar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Name and email addresses of recipients
ADMINS = (
    ('Edoardo Rossi', 'eddie@linuxbox'),
)

MANAGERS = ADMINS

VERSION = '0.2'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '484gwkp%2fd&s5^v+j(v(&okxc$pilh-z#l!(3qg)j!87kppz6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'djcelery',
    'playground',
)

import djcelery
djcelery.setup_loader()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'foobar.urls'

WSGI_APPLICATION = 'foobar.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'development': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     'USER': '', # Not used with sqlite3.
    #     'PASSWORD': '', # Not used with sqlite3.
    #     'HOST': '', # Set to empty string for localhost.
    #     # Not used with sqlite3.
    #     'PORT': '', # Set to empty string for default.
    #     # Not used with sqlite3.
    #     },
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'foobardb',
        'USER': 'dbuser',
        'PASSWORD': 'dbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FILE_CHARSET = 'utf-8'

# monday
FIRST_DAY_OF_WEEK = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = {
    'templates/',
}

LOG_FILE = os.path.join(BASE_DIR, 'logs/django.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     }
    # },
    'handlers': {
        # 'null': {
        #     'level': 'DEBUG',
        #     'class': 'logging.NullHandler',
        # },
        'console': {
            'level': 'WARN',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        #     # 'filters': ['special']
        # },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console','file'],
            'propagate': True,
            'level': 'ERROR',
        },
        'django.request': {
            'handlers': ['console','file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'playground.views': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            # 'filters': ['special']
        }
    }
}

ERROR_KEY = "ERROR"
