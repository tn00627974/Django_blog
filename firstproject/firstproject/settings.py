"""
Django settings for firstproject project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv # 導入 dotenv 套件

# from django.core.management.utils import get_random_secret_key
# print(get_random_secret_key())

# import sys
# print(sys.path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 獲取專案的根目錄
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = (os.path.join(BASE_DIR, 'SECRET_KEY'))
# 獲取 .env 檔案的路徑
load_dotenv(os.path.join(BASE_DIR, '.env')) # 同firstproject資料夾的.env 檔案

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# load_dotenv() 最外面的資料夾 

# print(os.getenv('DB_NAME'))
# print(os.getenv('DB_USER'))
# print(os.getenv('DB_PASS'))
# print(os.getenv('DB_HOST'))
# print(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['azure-django-web.azurewebsites.net']
# ALLOWED_HOSTS = ['127.0.0.1', 'azure-django-web.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myblog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware', # 靜態檔案加速
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "firstproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR / "templates")], # 加上 templates 目錄
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            'libraries' : {
                'my_tags' : 'myblog.my_tags',
            }
            
        },
    },
]

WSGI_APPLICATION = "firstproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# 本地端 測試資料庫設定
# DATABASES = {
#     "default": {
#         # "ENGINE": "django.db.backends.sqlite3",
#         # "NAME": BASE_DIR / "db.sqlite3",
#         # mysql
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "Django_Blog",
#         "USER": "root",
#         "PASSWORD": "password",
#         "HOST": "localhost",
#         "PORT": "3306",
#     }
# }

# Azure 遠端資料庫設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'), 
        'USER': os.getenv('DB_USER'), 
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'), # 資料庫主機名稱
        'PORT': '3306',
        'OPTIONS': {
            'ssl': {'ca': os.path.join('.\static\ssl\DigiCertGlobalRootCA.crt.pem')}  # 設定 SSL 連線  
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"
LANGUAGE_CODE = 'zh-hant' # 改為繁體中文
TIME_ZOME = 'Asia/Taipei' # 改為台北時區

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# 設定 static 靜態檔的路徑
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [ # 加入 static 路徑 
    os.path.join(BASE_DIR, 'static'), # 
    # BASE_DIR /'static',
]
STATIC_ROOT = os.path.join(BASE_DIR ,'staticfiles') # 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # 靜態檔案壓縮

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField" # 設定自動產生的 primary key 為 BigAutoField

