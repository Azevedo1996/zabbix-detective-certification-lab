from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-zabbix-detective-v2-local'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
INSTALLED_APPS = ['django.contrib.contenttypes', 'django.contrib.staticfiles', 'game']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]
ROOT_URLCONF = 'zabbix_detective.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': ['django.template.context_processors.request']},
}]
WSGI_APPLICATION = 'zabbix_detective.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
