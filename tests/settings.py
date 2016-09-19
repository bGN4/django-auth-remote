from __future__ import unicode_literals

import os
import posixpath


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGIN_URL = 'http://localhost:4430/login'
REDIRECT_FIELD_NAME = 'ref'

DEBUG = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'auth_remote.backends.RemoteAuthBackend',
)

SECRET_KEY = '@bGN4bGN4bGN4bGN4bGN4bGN4bGN4bGN4bGN4bGN4bGN4bGN4@'

ROOT_URLCONF = 'urls'

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

INSTALLED_APPS = [
    'app',
    'auth_remote',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    #'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]

#STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'root': {
        'handlers': ['console'],
    },
}
