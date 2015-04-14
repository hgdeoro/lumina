"""
Generated by 'django-admin startproject' using Django 1.8.
https://docs.djangoproject.com/en/1.8/topics/settings/
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# ===============================================================================
# Notes for 'production' settings for Lumina:
# ===============================================================================
#
# - LUMINA_DUMP_OBJECTS should be False
# - DEFAULT_FILE_STORAGE: TestImagesFallbackStorage should *NO* be used in prod.
#
# ===============================================================================

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't6m&zabdb8*f=5_n0nmc(5p5an8j@ipt48z&szzufxnf4v%1ha'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#
# Dump object with {% dump_objects %}
#
LUMINA_DUMP_OBJECTS = True

#
# AUTH_USER_MODEL = 'lumina.LuminaUser'
#
# Can't use AUTH_USER_MODEL:
#
# lumina (master)$ python manage.py migrate
# Running migrations for social_auth:
#  - Migrating forwards to 0002_auto__add_unique_nonce_timestamp_salt_server_u (...)
#  > social_auth:0001_initial
# ValueError: Cannot successfully create field 'user' for model 'usersocialauth':
#        "The model 'luminauser' from the app 'lumina' is not available in this migration.".
#

AUTH_USER_MODEL = 'lumina.LuminaUser'

DATETIME_FORMAT = 'd/m/Y - H:i'

# SOUTH_MIGRATION_MODULES = {
#     'social_auth': 'ignore',
# }

# # http://south.readthedocs.org/en/latest/settings.html#south-tests-migrate
# SOUTH_TESTS_MIGRATE = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.expanduser('~/lumina.sqlite'),
    }
}

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Cordoba'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django 1.8 -> hace falta esto?
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.expanduser('~/lumina/uploads/')

MEDIA_URL = ''

STATIC_ROOT = ''

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'lumina.middleware.LoggingMiddleware',
)

ROOT_URLCONF = 'lumina.urls'

WSGI_APPLICATION = 'lumina.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # ----- Django 1.8 defaults
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # ----- Migrated from old config / Django 1.5
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                # "social_auth.context_processors.social_auth_by_name_backends", # LUMINA_NOSOCIAL
            ],
        },
    },
]

# Application definition

INSTALLED_APPS = (
    # ----- Django 1.8 defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ----- Migrated from old config / Django 1.5
    'django.contrib.humanize',
    # 'localflavor',
    # 'cities_light',
    'autocomplete_light',
    'lumina',
    'mailer',
    # 'social', # LUMINA_NOSOCIAL
    # 'social_auth', # LUMINA_NOSOCIAL
)


# Path to look for web driver executable
SELENIUM_WEBDRIVER_BIN = (
    # Ubuntu 13.04 - Package: 'chromium-chromedriver'
    '/usr/lib/chromium-browser/chromedriver',
)


# Default:
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FILE_STORAGE = 'lumina.django_files_storage.TestImagesFallbackStorage'


AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend', # LUMINA_NOSOCIAL
    #    'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend', # LUMINA_NOSOCIAL
    #    'social_auth.backends.google.GoogleOAuth2Backend',
    #    'social_auth.backends.google.GoogleBackend',
    #    'social_auth.backends.yahoo.YahooBackend',
    #    'social_auth.backends.browserid.BrowserIDBackend',
    #    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #    'social_auth.backends.contrib.disqus.DisqusBackend',
    #    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    #    'social_auth.backends.contrib.orkut.OrkutBackend',
    #    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    #    'social_auth.backends.contrib.github.GithubBackend',
    #    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    #    'social_auth.backends.contrib.live.LiveBackend',
    #    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    #    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    #    'social_auth.backends.contrib.readability.ReadabilityBackend',
    #    'social_auth.backends.contrib.fedora.FedoraBackend',
    #    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = 'home'

#
# SOCIAL_AUTH_LOGIN_REDIRECT_URL
# Where to redirect after an existing user was identified
#
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

#
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL
# Where to redirect after a new user was created
#
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/?SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/?SOCIAL_AUTH_DISCONNECT_REDIRECT_URL'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/?SOCIAL_AUTH_BACKEND_ERROR_URL'
SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_INACTIVE_USER_URL = '/?SOCIAL_AUTH_INACTIVE_USER_URL'

# SERVER_EMAIL = 'notifications@lumina-photo.com.ar'
# DEFAULT_FROM_EMAIL = 'Lumina <notifications@lumina-photo.com.ar>'
# EMAIL_HOST_USER = 'notifications@lumina-photo.com.ar'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
# Email Test Server: python -m smtpd -n -c DebuggingServer localhost:1025

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
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
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Googgle allows us to use OAuth without key/secret
# See: http://django-social-auth.readthedocs.org/en/latest/backends/google.html#google-oauth
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''


if os.environ.get("LUMINA_TEST_SKIP_MIGRATIONS", "0") == "1":
    NOT_USED = "lumina_migrations_not_used_in_tests"
    MIGRATION_MODULES = {"lumina": NOT_USED,
                         "contenttypes": NOT_USED,
                         "admin": NOT_USED,
                         "auth": NOT_USED,
                         "sessions": NOT_USED,
                         }


try:
    from lumina.local_settings import *  # noqa
except ImportError as e:
    import warnings
    warnings.warn("Couldn't import from 'lumina.local_settings': %s" % e.args[0], stacklevel=0)
    TWITTER_CONSUMER_KEY = ''
    TWITTER_CONSUMER_SECRET = ''
