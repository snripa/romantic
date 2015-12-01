# coding=utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, random
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

SECRET_KEY = '=q@eild4ch4mg#lyso0^^gnd4r2bc&@lj*sw=ua1gpe$#ua4x6'

DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
    ('Dmitry Lyapun', 'dlyapun@gmail.com'),
)
MANAGERS = ADMINS

ALLOWED_HOSTS = [
    '127.0.0.1:8000',
    '.example.com',
    '.tkr.od.ua',
]

INTERNAL_IPS = ("127.0.0.1",)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

for root, dirs, files in os.walk(PROJECT_ROOT):
    if 'templates' in dirs:
        TEMPLATE_DIRS += (os.path.join(root, 'templates'),)

INSTALLED_APPS = (
    'jet.dashboard',
    'jet',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hike',
    'profile',
    'imagekit',
    'party',
    'force_blog',
    'bootstrap_pagination',
    'power_comments',
    'banner',
    'page_navigation',
    'materials',
    'django_summernote',
    'info_pages',
    'django_cleanup',
    'redactor',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    'profile.context_processor.contex_profile',
    'info_pages.context_processor.contex_info_pages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'romantic.urls'

WSGI_APPLICATION = 'romantic.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ukrainem_tkr2",
        "USER": "ukrainem_tkr",
        "PASSWORD": "qwerty123456",
        "HOST": "10.0.0.2",
        "PORT": "",
    }
}


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = '/home/ukrainem/domains/tkr.od.ua/public_html/media/'
STATIC_ROOT = '/home/ukrainem/domains/tkr.od.ua/public_html/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

try:
    from local_settings import *
except ImportError:
    pass


try:
    from summernote_settings import *
except ImportError:
    pass


try:
    from power_comments.settings import *
except ImportError:
    pass

SOCIAL_AUTH_FACEBOOK_KEY = '1602017563346275'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ebc2b04baf9d0421d766d31be62e8e2b'

SOCIAL_AUTH_TWITTER_KEY = 'eYzXFuk4K4L0siJwp7w9wm1Yt'
SOCIAL_AUTH_TWITTER_SECRET = 'qfHHktIzkvToq1dQeYxZY8udhUzVlMFtjBa9TzOTc5NnTimyoU'

LOGIN_URL = '/login/'
LOGOUT_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/blog/'

SOCIAL_AUTH_VK_APP_KEY = '4816303'
SOCIAL_AUTH_VK_OAUTH2_KEY = '4816303'
SOCIAL_AUTH_VK_APP_SECRET = '5HO4lXQiwRRfuoAFI4mh'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '5HO4lXQiwRRfuoAFI4mh'

AUTH_PROFILE_MODULE = "profile.CustomUser"

DEFAULT_BANNER_TITLE = 3

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'support@tkr.od.ua'
EMAIL_USE_TLS = True
EMAIL_HOST = '148.251.236.139'
EMAIL_HOST_USER = 'support@tkr.od.ua'
EMAIL_HOST_PASSWORD = 'blasco5454588407'
EMAIL_PORT = 587
SERVER_EMAIL = 'support@tkr.od.ua'

REDACTOR_OPTIONS = {'lang': 'ru'}
REDACTOR_UPLOAD = 'uploads/'
