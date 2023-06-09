"""
Django settings for BarbieSalon project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0wak4vxc-5oc#nb!!k6z#+zf1aq##2+wgg6ou-4&d#is9s$%sj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', '10.1.45.235', '*']
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_PROXY_SSL_HEADER = True



# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'adminlte3',
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CustomerView',
    'dashboard',
    'users',
    'tinymce',
    'fontawesomefree',
    'crispy_forms',
    'captcha',
    'rest_framework',
]
AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BarbieSalon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'BarbieSalon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'users-login'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = ['users.backends.EmailBackend']

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# domain == 127.0.0.1
# RECAPTCHA_PUBLIC_KEY = '6LeSFvojAAAAAC9yiXTwvOHPm-Tps7Hq10H3tnnQ'
# RECAPTCHA_PRIVATE_KEY = '6LeSFvojAAAAAB2uCzYt7IV1LSwK7MV0zgAllTtb'

# domain == 10.1.135.119
RECAPTCHA_PUBLIC_KEY = '6LfF6gMkAAAAAMc3HKXOa6OMbAiodC6K7lBB3RS2'
RECAPTCHA_PRIVATE_KEY = '6LfF6gMkAAAAAM4P1f3GCFW_JXZx1LUJFmUtonPi'


# # domain == 10.1.45.235
# RECAPTCHA_PUBLIC_KEY = '6LdXO_wjAAAAAFrZ0JKx8xFKzcv20ACpb8NIMo6h'
# RECAPTCHA_PRIVATE_KEY = '6LdXO_wjAAAAAOE5uEo-pGZts3OBMg7SgxpqejD7'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# recaptcha v3 keys
# domain == 127.0.0.1
# RECAPTCHA_PUBLIC_KEY = '6LfDF_ojAAAAAKBoGBvKHQ5775KueMTKAg9RG4DQ'
# RECAPTCHA_PRIVATE_KEY = '6LfDF_ojAAAAABA5ncVpJN2BcDf08bWikkzeHLOP'

# Emailing settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'terahjones3@gmail.com'
SERVER_EMAIL = 'terahjones3@gmail.com'
EMAIL_HOST_USER = 'terahjones3@gmail.com'
EMAIL_HOST_PASSWORD = 'kqphvumaohdwfruc'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
PASSWORD_RESET_TIMEOUT = 14400

TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 100,
    'selector': 'textarea',
    "menubar": "file edit view insert format tools table help",
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'undo redo | backcolor casechange permanentpen formatpainter removeformat formatselect fontselect '
                'fontsizeselect',
    'toolbar2': 'bold italic underline blockquote | alignleft aligncenter alignright alignjustify '
                '| bullist numlist | outdent indent | table | link image | codesample | preview code |'
                'tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry',
    'contextmenu': 'formats | link image',
    'block_formats': 'Paragraph=p; Header 1=h1; Header 2=h2',
    'fontsize_formats': "8pt 10pt 12pt 14pt 16pt 18pt",
    'content_style': "body { font-family: Arial; background: white; color: black; font-size: 12pt}",
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'}, {'text': 'HTML/XML', 'value': 'markup'}, ],
    'image_class_list': [{'title': 'Fluid', 'value': 'img-fluid', 'style': {}}],
    'width': 'auto',
    "height": "300px",
    'image_caption': True,
}
