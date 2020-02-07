from corsheaders.defaults import default_headers
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import os

try:
    from .local import *
except ImportError:
    import dj_database_url
    from decouple import config

    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = ['tree-con.herokuapp.com']

    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }
    # SECURE_SSL_REDIRECT = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    # SECURE_HSTS_SECONDS = 15768000
    # SECURE_BROWSER_XSS_FILTER = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # X_FRAME_OPTIONS = 'DENY'
    # SECURE_HSTS_PRELOAD = True
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    pass


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    'django_filters',
    "allauth",
    "allauth.account",
    "rest_auth",
    "admin_honeypot",
    'django_extensions',
    
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
]

if not DEBUG:
    INSTALLED_APPS.insert(0, "scout_apm.django")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "project.wsgi.application"

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# allauth settings

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGOUT_ON_PASSWORD_CHANGE = False
LOGIN_REDIRECT_URL = "/"



LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# static and media
# if STATIC_ROOT ends with STATIC_URL, it makes nginx static serve config easy, likewise for media
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "COERCE_DECIMAL_TO_STRING": False,
}


# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + ("content-disposition",)

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://tree-con.netlify.com"
]

SCOUT_NAME = "TreeCon"

SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PRINT_SQL_TRUNCATE = None

SHELL_PLUS_SQLPARSE_FORMAT_KWARGS = dict(
  reindent_aligned=True,
)

sentry_sdk.init(
    dsn="https://ce935786a77d497db2db4258364905cb@sentry.io/2166643",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
