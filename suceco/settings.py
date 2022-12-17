import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'local'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'species.apps.SpeciesConfig',
    'forest.apps.ForestConfig',
    'register.apps.RegisterConfig',
    'contact.apps.ContactConfig',
    'reference.apps.ReferenceConfig'
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'suceco.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join((BASE_DIR), 'templates/')],
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

WSGI_APPLICATION = 'suceco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, 
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'suceco_log.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        }
    },

    'loggers': {

        '': {
            'level': 'ERROR',
            'handlers': ['console'],
        },

        'species': {
            'level': 'ERROR',
            'handlers': ['file', 'console'],
            'propagate': False
        },

        'forest' : {
            'level' : 'ERROR',
            'handlers' : ['file', 'console'],
            'propagate' : False
        },

        'register' : {
            'level' : 'ERROR',
            'handlers' : ['file', 'console'],
            'propagate' : False
        },
        'contact' : {
            'level' : 'ERROR',
            'handlers' : ['file', 'console'],
            'propagate' : False
        },

        'noisy_module': {
            'level':'ERROR',
            'handlers': ['console'],
            'propagate': False
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# EMAIL CONFIG DEFAULT
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL CONFIG AWS SES - AWS SIMPLE EMAIL SERVICE
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = os.environ.get('REGION')
AWS_SES_REGION_ENDPOINT = os.environ.get('REGION_ENDPOINT')
USE_SES_V2 = True
EMAIL_FROM = os.environ.get('EMAIL_FROM')
EMAIL_DESTINATION = os.environ.get('EMAIL_DESTINATION')