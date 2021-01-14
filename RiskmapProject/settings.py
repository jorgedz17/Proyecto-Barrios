import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") #Configurar el env en el servidor
#DEBUG = int(os.environ.get("DJANGO_DEBUG", default=0)) #Configurar el env en el servidor
#ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")#Configurar el env en el servidor

#Para uso local
DEBUG=1
SECRET_KEY="8p35_)j1p$#ruh0y^pptlro1z@%@ia&=8&fuqx!%5drp2&1w%1"
ALLOWED_HOSTS='*'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'dashboard',
    'userprofiles',
]
#AUTH_USER_MODEL = 'RiskmapApp.CustomUser' #modelo custom del profe, desactivado para este proyecto pero conservado por futuros usos
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'RiskmapProject.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
WSGI_APPLICATION = 'RiskmapProject.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
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
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = False
STATIC_URL = '/staticfiles/'
STATICFILES_DIRS= [os.path.join(BASE_DIR,"staticfiles"), ]
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


#SESSION_COOKIE_AGE = int(os.environ.get("DJANGO_SESSION_COOKIE_AGE"))
SESSION_COOKIE_AGE=900
#SESSION_COOKIE_SAMESITE = 'Strict'
#SESSION_COOKIE_SECURE = True
