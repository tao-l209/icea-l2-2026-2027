# settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète : à mettre dans une variable d'environnement en production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'changez-moi-en-production')
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # vos apps ici
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'monprojet.urls'
WSGI_APPLICATION = 'monprojet.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ============ CONNEXION MYSQL (phpMyAdmin) ============
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nom_de_la_base',        # nom de la base vue dans phpMyAdmin
        'USER': 'root',                  # utilisateur MySQL
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': '127.0.0.1',             # ou 'localhost'
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
# =======================================================

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'America/Martinique'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'