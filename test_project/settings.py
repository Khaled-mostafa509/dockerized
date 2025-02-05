"""
Django settings for test_project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import dj_database_url
from pathlib import Path
import os
#import django_heroku
import dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
AUTH_USER_MODEL = 'authentications.User'
# ACCOUNT_UNIQUE_EMAIL= True


INSTALLED_APPS = [
    # 'modeltranslation',
    'authentications',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'home',
    'helpers',
    'rest_framework.authtoken',
    'bootstrap4',
    'django_forms_bootstrap',
    'django_filters',
    # 'embed_video',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.locale.LocaleMiddleware'
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    # )
}

ROOT_URLCONF = 'test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'test_project.wsgi.application'
CSRF_TRUSTED_ORIGINS = ["https://gradproject.azurewebsites.net",
                        "https://www.gradproject.azurewebsites.net"]

# DATABASES = {

#     'default': {

#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': 'd98pb6ma2qn6l7',

#         'USER': 'pygpluhxryacul',

#         'PASSWORD': '9ade93b175f110fda0b9c9d3b135d0eb053b842b3c8690c3f0f300b4d2086427',

#         'HOST': 'ec2-34-239-241-121.compute-1.amazonaws.com',

#         'PORT': '5432'

#     },
# DATABASES = {

#     'default': {

#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': 'd2u0c4ugqvmigm',

#         'USER': 'inpigxugpfdnku',

#         'PASSWORD': '8c0a56bf419271b79ced61bf525497122ee391b20b2f92097c26cbdd6b706ab9',

#         'HOST': 'ec2-23-23-182-238.compute-1.amazonaws.com',

#         'PORT': '5432'

#     }

# }
# }
# DATABASES = {

#     'default': {

#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': 'd9cimr5l93ei1g',

#         'USER': 'ufstawsuwnzjyc',

#         'PASSWORD': '2c62f4ebfaf84806122c0aef0e91247420540e45fc7749eec3b0bb73ea6213e5',

#         'HOST': 'ec2-44-196-174-238.compute-1.amazonaws.com',

#         'PORT': '5432'

#     }

# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#dj_heroku = dj_database_url.config(conn_max_age=600)

#DATABASES['default'].update(dj_heroku)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# def gettext(s): return s


# LANGUAGES = (
#     ('de', gettext('German')),
#     ('en', gettext('English')),
# )

# LOCALE_PATHS = [
#     BASE_DIR / 'locale/',
# ]

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
# MODELTRANSLATION_LANGUAGES = ('de', 'en')

# MODELTRANSLATION_TRANSLATION_FILES = (
#     'home.translation',
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    'static/',
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#django_heroku.settings(locals())
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'khaledmostafa5509@gmail.com'
EMAIL_HOST_PASSWORD = 'vutigtschjbmzyds'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'

# IS_MONOLINGUAL = False
# TRANSLATABLE_MODEL_MODULES = ["home.models"]
