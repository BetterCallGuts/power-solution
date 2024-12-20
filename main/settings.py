from pathlib import Path
import os
from django.contrib.messages import constants as messages
BASE_DIR       = Path(__file__).resolve().parent.parent
SECRET_KEY     = 'django-insecure-05ypsjz$tkn5y#aq$3430#9fqqbdns$j3@gc7ab^e5_@-mz6vy'
DEBUG          = True
ALLOWED_HOSTS  = ["*"]
INSTALLED_APPS = [
    "jazzmin"                    ,
    'django.contrib.admin'       ,
    'django.contrib.auth'        ,
    'django.contrib.contenttypes',
    'django.contrib.sessions'    ,
    'django.contrib.messages'    ,
    'django.contrib.staticfiles' ,
    "core"                       ,
] 
MESSAGE_TAGS   = {
    messages.DEBUG   : 'alert-secondary',
    messages.INFO    : 'alert-info',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
    messages.ERROR   : 'alert-danger',
}

MIDDLEWARE     = [
    'django.middleware.security.SecurityMiddleware',
    'core.middleware.ForceCustom404Middleware',  

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF   = 'main.urls'
TEMPLATES      = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "core.context.global_variables",
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

DATABASES        = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS  = [
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


LANGUAGE_CODE      = 'en-us'
TIME_ZONE          = 'UTC'
USE_I18N           = True
USE_TZ             = True

STATIC_URL         = 'static/'
STATIC_ROOT        =  os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS   = [os.path.join(BASE_DIR, 'static_dir')]

MEDIA_URL          = 'media/'
MEDIA_ROOT         = os.path.join(BASE_DIR, 'media_root')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
