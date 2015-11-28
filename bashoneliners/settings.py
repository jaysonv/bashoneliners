"""
Django settings for bashoneliners project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(p^8-@2q(uck=2+fph+1pxx=)4lrl)_!p%7b9m1&#qoy%+9+v6'

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
    'social.apps.django_app.default',
    'oneliners',
    'accounts',
    'django_openid_auth',
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

ROOT_URLCONF = 'bashoneliners.urls'

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

WSGI_APPLICATION = 'bashoneliners.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


# Example:
# import logging
# logger = logging.getLogger(__name__)
# logger.debug('something happened')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'debug.log'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'oneliners': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}


# project specific django settings

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'oneliners.context_processors.google_analytics',
)

# AUTH_PROFILE_MODULE = 'oneliners.models.HackerProfile'

AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.stackoverflow.StackoverflowOAuth2',
    'social.backends.yahoo.YahooOpenId',
    'social.backends.yahoo.YahooOAuth2',
    'social.backends.yahoo.YahooOAuth',
    'social.backends.launchpad.LaunchpadOpenId',
    'social.backends.open_id.OpenIdAuth',
    'django.contrib.auth.backends.ModelBackend',
)

#OPENID_CREATE_USERS = True
#OPENID_UPDATE_DETAILS_FROM_SREG = True

#LOGIN_URL = '/accounts/login/'
#LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/oneliners/'
SOCIAL_AUTH_LOGIN_URL = '/'

# http://python-social-auth.readthedocs.org/en/latest/backends/google.html#google-openid
# Go to Google Developer Console: https://console.developers.google.com/
# Go to API Manager, enable Google+ API
# Go to API Manager / Credentials
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

# http://python-social-auth.readthedocs.org/en/latest/backends/github.html
# https://github.com/settings/applications/new
SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''

# http://python-social-auth.readthedocs.org/en/latest/backends/twitter.html
# https://realpython.com/blog/python/adding-social-authentication-to-django/
# Go to https://apps.twitter.com/app/new
# As callback url specify: http://127.0.0.1:8000/complete/twitter
# Go to Keys and Access Tokens tab
# SOCIAL_AUTH_TWITTER_KEY = Consumer Key (API Key)
# SOCIAL_AUTH_TWITTER_SECRET = Consumer Secret (API Secret)
# Test with http://127.0.0.1:8000/login/twitter
SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''

# http://python-social-auth.readthedocs.org/en/latest/backends/stackoverflow.html
# https://api.stackexchange.com/
# http://stackapps.com/apps/oauth/register
# Note: the OAuth Domain must match the domain where the site is running
SOCIAL_AUTH_STACKOVERFLOW_KEY = ''
SOCIAL_AUTH_STACKOVERFLOW_SECRET = ''
SOCIAL_AUTH_STACKOVERFLOW_API_KEY = ''

# Yahoo works out of the box:
# http://127.0.0.1:8000/login/yahoo

# Launchpad works out of the box:
# http://127.0.0.1:8000/login/launchpad

# project specific custom settings

# sending emails
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(LOGS_DIR, 'emails.log')
EMAIL_BACKEND = 'oneliners.email.CustomFileEmailBackend'

# url shortening
#
GOO_GL_API_URL = 'https://www.googleapis.com/urlshortener/v1/url'
GOO_GL_API_KEY = ''

# google analytics
GOOGLE_ANALYTICS_ID = 'UA-XXXXXXXX-X'
