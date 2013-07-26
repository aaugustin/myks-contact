# Only used for running the tests

import os

CONTACT_EMAILS = ['charlie@example.com']

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = ['contact']

ROOT_URLCONF = 'contact.tests.urls'

SECRET_KEY = 'whatever'

TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__), 'templates')]
