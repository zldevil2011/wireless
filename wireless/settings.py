"""
Django settings for wireless project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_PATH = './media'
STATIC_ROOT = './static/'
MEDIA_ROOT = './media/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '85hxn6e7s-87(ij!7u3$o1#@*pt!32dx8!l*1nukjb92_rpv9&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'app',
	'rest_framework',
	'oauth2_provider',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wireless.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wireless.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wireless',
		'USER': 'wsn',
		'PASSWORD':'wsn3037',
		'HOST': 'localhost',
		'PORT': '3306',
		#'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'zldevil2011@163.com'
EMAIL_HOST_PASSWORD = 'a1234567890'
EMAIL_SUBJECT_PREFIX = '[12Golf]'
EMAIL_USE_TLS = False
SERVER_EMAIL = 'zldevil2011@163.com'

#MEMCACHE
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION' : '127.0.0.1:11211',
	}
}

#REST_FRAMEWORK = {
#	'DEFAULT_PERMISSION_CLASSES':(
#		#'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#		'rest_framework.permissions.IsAdminUser',	
#	),
#	'PAGE_SIZE':10
#}

#OAUTH2
OAUTH2_PROVIDER = {
	'ACCESS_TOKEN_EXPIRE_SECONDS' : 60 * 60 * 24 * 360 * 100,
	'AUTHORIZATION_CODE_EXPIRE_SECONDS' : 60 * 60 * 24 * 360 * 100,
	'SCOPES': {'read' : 'Read scope', 'write' : 'Write scope', 'groups' : 'Access to your groups'}
}

OAUTH_APPLICATION_NAME = 'wireless'
OAUTH2_GET_TOKEN_URL = 'http://127.0.0.1/o/token/'
OAUTH2_REVOKE_TOKEN_URL = 'http://127.0.0.1/o/revoke_token/'
