"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.1.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
#from yookassa import Configuration
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i8t-^!74-#_b-m3u@n)6t64vzktr)dx=h7b%t_wg85fre(cw04"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'stripe',
    'coupons.apps.CouponsConfig',
    
    
    
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myshop.urls"

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
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "myshop.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "perfums",
        "USER": 'perfume_admin',
        "PASSWORD": 'qwerty',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/



LANGUAGE_CODE = 'ru'

"""LOCALE_PATHS = [
    BASE_DIR / 'locale',
]"""

TIME_ZONE = 'Europe/Moscow'
#TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'static'


CART_SESSION_ID = 'cart'



STRIPE_PUBLISHABLE_KEY = 'pk_test_51NzRyJCd6dWw2lbBvV1Qu8E9pOOdkiNQfHuC1AlfSL28AVCc2hwiYsUkaKVgosvJoVn6d9WfsxLwdNysXpDzbGPA00OdqDH3rT' 
STRIPE_SECRET_KEY = 'sk_test_51NzRyJCd6dWw2lbBs4CgLfIkTew7JxNVAmhptCyp4ETbRZy0lzzTz26WOCvo0s9WQ10ofLlRPL4Xb31P1M6BLPfH00VZfHZU5T' 
STRIPE_API_VERSION = '2022-08-01' 
STRIPE_WEBHOOK_SECRET = 'whsec_3399fe96f6f7eebaee04f8aad4aa671857f4ba77910081cfbf0071a1c42f2afd'



YANDEX_KASSA_SHOP_ID = '274933'
YANDEX_KASSA_SECRET_KEY = 'test_1ytArpck6tOLy96Y5--5KPdELWzeYWuwkeqmHBixWZI'
YANDEX_KASSA_SCID = '274932'
YANDEX_KASSA_TEST_MODE = True

#Configuration.account_id = '274933'
#Configuration.secret_key = 'test_1ytArpck6tOLy96Y5--5KPdELWzeYWuwkeqmHBixWZI'

YOO_KASSA = {
    'ACCOUNT_ID': '274933',
    'SECRET_KEY': 'test_1ytArpck6tOLy96Y5--5KPdELWzeYWuwkeqmHBixWZI',
    'IS_TEST_MODE': True  # Рекомендуется использовать тестовый режим для начала
} 


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1


"""PARLER_LANGUAGES = {
    None: (
        {'code': 'ru'},
        {'code': 'en'},
        
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}"""