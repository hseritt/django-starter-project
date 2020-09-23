import logging
import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key
# SECRET_KEY = get_random_secret_key()
SECRET_KEY = "foobar"  # Don't use this in production.
# Generate your own with
# the get_random_secret_key function.

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/3.0/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


# Application definition
# https://docs.djangoproject.com/en/3.0/ref/settings/#installed-apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "django_starter.example",
    "django_starter.apps.registration",
]

# https://docs.djangoproject.com/en/3.0/topics/http/middleware/
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# https://docs.djangoproject.com/en/3.0/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# https://docs.djangoproject.com/en/3.0/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "django_starter", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# https://docs.djangoproject.com/en/3.0/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_starter",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "db",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "django_starter", "static"),
]


# https://docs.djangoproject.com/en/3.0/ref/settings/#login-url
LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/auth/login/"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        "rest_framework.permissions.AllowAny",
        # 'rest_framework.permissions.IsAuthenticated',
    ],
}

CORS_ORIGIN_ALLOW_ALL = True
# OR

"""
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
)
"""


# Logging settings
LOGGING_FORMAT = (
    "%(asctime)s  [%(levelname)s]  [%(module)s.%(name)s.%(funcName)s]:%(lineno)s"
    "  %(message)s"
)
LOGGING_LEVEL = logging.DEBUG  # lowest level logged as a whole.
LOG_FILE = "django_starter.log"
LOG_FILE_WRITE_MODE = "w"  # w or a for write or append.


# Email settings
# Set your smtp login in environment variables for:
# TEST_EMAIL_ACCOUNT and TEST_EMAIL_PASSWORD
# Ex: export TEST_EMAIL_ACCOUNT=harlin@gmail.com
# Ex: export TEST_EMAIL_PASSWORD=myS3cr3t
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("TEST_EMAIL_ACCOUNT")
EMAIL_HOST_PASSWORD = os.environ.get("TEST_EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("TEST_EMAIL_ACCOUNT")
DEFAULT_TO_EMAIL = os.environ.get("TEST_EMAIL_ACCOUNT")
