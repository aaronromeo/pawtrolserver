"""
Django settings for pawtrolserver project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# For the PSQL connection...
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '%=h=o1hb&dj1vqh6^puy=xw!rb%-=22psfdvf#_aypjujmfo2o')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DEBUG', 0))

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"), )
TEMPLATE_DEBUG = bool(os.getenv('DEBUG', 0))

# ALLOWED_HOSTS = ['.pawtrolapp.com', '.pawtrol.co']
ALLOWED_HOSTS = []

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)

# Application definition

AUTH_USER_MODEL = 'profiles.User'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'django_extensions',
    'corsheaders',
    'rest_framework',
    'djcelery',

    # Me! Me! Me!
    'common',
    'profiles',    
    'api',
    'billing',
    'feedback',
    'petservices',

    # This has been moved after the installation of the app as the rest_framework.authtoken
    # requires the 'app' migrations to run before it can complete.
    'rest_framework.authtoken',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pawtrolserver.urls'

WSGI_APPLICATION = 'pawtrolserver.wsgi.application'

# TODO: Verify this!
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default="postgis://{}:{}@{}/{}".format(
            os.getenv('DB_USER'),
            os.getenv('DB_PASS'),
            os.getenv('DB_SERVER', 'localhost'),
            os.getenv('DB_NAME')
        )
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static/')

STATICFILES_DIRS = (
)

# A subclass of the StaticFilesStorage storage backend which stores the file names it handles by appending the MD5 hash of 
# the file's content to the filename. For example, the file css/styles.css would also be saved as css/styles.55e7cbb9ba48.css.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media/')

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# AWS_S3_SECURE_URLS = False                                  # use http instead of https
# AWS_QUERYSTRING_AUTH = False                                # don't add complex authentication-related query parameters for requests
# AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')    # enter your access key id
# AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')    # enter your secret access key
# AWS_STORAGE_BUCKET_NAME = 'pawtrol'

ADMINS = (('Aaron', 'aaron@pawtrol.co'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '{}/pawtrolserver_django_debug.log'.format(os.getenv('LOG_DIR', os.path.join(os.path.dirname(os.path.dirname(PROJECT_ROOT)), 'logs/'))),
        },
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        },        
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'file',
                'console',
                'mail_admins',
            ],
            'propagate': True,
            'level': 'WARNING',
        },
        'django.request': {
            'handlers': [
                'file',
                'console',
                'mail_admins',
            ],
            'level': 'ERROR',
            'propagate': False,
        },
        'api': {
            'handlers': [
                'file',
                'console',
                'mail_admins',
            ],
            'level': 'INFO'
        },
        'web': {
            'handlers': [
                'file',
                'console',
                'mail_admins',
            ],
            'level': 'INFO',
        },
    },
}

MIGRATION_MODULES = {
    'sites': 'pawtrolserver.fixtures.sites_migrations',
}

SERVER_EMAIL = 'django@pawtrol.co'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EVENT_DATE = os.getenv('EVENT_DATE', '')

