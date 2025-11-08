"""
Django settings for core project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Load environment variables
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# SECURITY SETTINGS
# ==============================
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key')  # safer than hardcoding

DEBUG = False  # must be False for production

ALLOWED_HOSTS = ['*']  # later you can change this to your render domain

# ==============================
# INSTALLED APPS
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # GSO Apps
    'apps.gso_accounts',
    'apps.gso_requests',
    'apps.gso_inventory',
    'apps.gso_reports',
    'apps.gso_migration',
    'apps.notifications',
    'apps.ai_service',

    'core',

    # Third-party apps
    "widget_tweaks",
]

# ==============================
# MIDDLEWARE
# ==============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise for static files in Render
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# ==============================
# TEMPLATES
# ==============================
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

WSGI_APPLICATION = 'core.wsgi.application'

# ==============================
# DATABASE
# ==============================
# Use Neon.tech database if DATABASE_URL is set, otherwise local Postgres
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'psql 'postgresql://neondb_owner:npg_sa9njfRPd3BA@ep-red-field-a46slt7r-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require''),
        conn_max_age=600
    )
}

# ==============================
# PASSWORD VALIDATORS
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================
# INTERNATIONALIZATION
# ==============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'  # better for PSU
USE_I18N = True
USE_TZ = True

# ==============================
# STATIC & MEDIA FILES
# ==============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ==============================
# AUTHENTICATION
# ==============================
AUTH_USER_MODEL = "gso_accounts.User"
LOGIN_REDIRECT_URL = '/gso_accounts/redirect/'
LOGIN_URL = '/gso_accounts/login/'
LOGOUT_REDIRECT_URL = '/gso_accounts/login/'

# ==============================
# CUSTOM SETTINGS
# ==============================
HF_API_KEY = os.getenv("HUGGINGFACE_API_TOKEN")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
