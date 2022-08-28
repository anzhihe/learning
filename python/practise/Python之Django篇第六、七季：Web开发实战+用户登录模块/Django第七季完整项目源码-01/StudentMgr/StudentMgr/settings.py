"""
Django settings for StudentMgr project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# 添加一个目录
sys.path.append(os.path.join(BASE_DIR, 'apps'))
sys.path.append(os.path.join(BASE_DIR, 'apps', 'web'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#jvq+%y6hupfgu6&5b#v$e^)2k5f@j-dyp5gqgq!w%nwkxcoxj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basicweb',
    'mainweb',
    'studentweb',
    'userweb',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # 负责csrftoken校验
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # x-frame标签
    # ==== 注册中间件 ======
    'userweb.middleware.auth.Auth_Md',
]

ROOT_URLCONF = 'StudentMgr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'apps', 'resources_base', 'templates_base'),
        ],
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

WSGI_APPLICATION = 'StudentMgr.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_v7_db',
        'USER': 'root',
        'PASSWORD': '1234.Com',
        'HOST': '192.168.182.10',
        'PORT': '3306',
    }
}

# ====redis的配置=====
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.182.10:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": "1234.Com",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 上传文件的路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'apps', 'upload')  # 内部存储的根目录  --- 本地磁盘
MEDIA_URL = '/upload/'  # 外部访问的根目录 --- url

# ========= 注册静态目录 ====
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps', 'static'),
]

# ========= 设置X-Frame-Option选项======
X_FRAME_OPTIONS = "SAMEORIGIN"

# 全局的设定在django的settings中设定, 具体设置如下：
SESSION_COOKIE_AGE = 14 * 24 * 3600  # 30分钟
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 关闭浏览器，则COOKIE仍有效

# ================= 配置邮箱 =================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True  # 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = False  # 是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.qq.com'  # 发送邮件的邮箱 的 SMTP服务器，这里用了qq邮箱
EMAIL_PORT = 25  # 发件箱的SMTP服务器端口
EMAIL_HOST_USER = '651205558@qq.com'  # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'hyvxzmigilmxbbab'  # 发送邮件的邮箱密码(这里使用的是授权码)

# ===========设置URL白名单 =========
WHITE_URL_LIST = [
    '/user/login/',
    '/user/login/handle/',
    '/user/reset/pass/',
    '/user/reset/pass/get_account/',
    '/user/reset/pass/send_email/',
    '/user/reset/pass/check_code/',
    '/user/reset/pass/commit/',
]
