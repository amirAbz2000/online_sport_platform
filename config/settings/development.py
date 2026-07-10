"""
تنظیمات محیط توسعه
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database - SQLite برای سهولت توسعه
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email backend - چاپ ایمیل‌ها در کنسول
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debug toolbar (می‌توانید بعداً نصب کنید)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
# INTERNAL_IPS = ['127.0.0.1']
