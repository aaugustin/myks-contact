# Only used for running the tests

import os

CONTACT_EMAILS = ['charlie@example.com']

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = ['contact', 'django.contrib.staticfiles']

ROOT_URLCONF = 'contact.test_urls'

SECRET_KEY = 'whatever'

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'test_templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
            ],
        },
    },
]
