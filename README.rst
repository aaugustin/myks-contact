mYk's contact form
==================

Goals
-----

`myks-contact`_ is a simple contact form. It's adequate for a personal home
page. It features a basic CAPTCHA_.

.. _myks-contact: https://github.com/aaugustin/myks-contact
.. _CAPTCHA: http://en.wikipedia.org/wiki/Captcha

Setup
-----

myks-contact is a pluggable Django application. It is tested with Django ≥ 1.8.

1.  Download and install the package from PyPI::

        $ pip install myks-contact

2.  Add ``contact`` to ``INSTALLED_APPS``::

        INSTALLED_APPS += ['contact']

    This allows Django to discover the built-in templates and translations.

3. Define the list of recipients in the ``CONTACT_EMAILS`` setting::

        CONTACT_EMAILS = ['you@example.com']

4.  Add the application to your URLconf with the ``contact`` application
    namespace::

        urlpatterns += [
            url(r'^contact/', include('contact.urls', namespace='contact', app_name='contact')),
        ]

To use the built-in templates, your project's ``base.html`` template must
provide three blocks: ``title``, ``extrahead`` and ``content``, as shown in
this `example`_, and you must be using the staticfiles contrib app.

If these conditions are inconvenient, you can override the
``contact/form.html`` and ``contact/thanks.html`` templates.

.. _example: https://github.com/aaugustin/myks-contact/blob/master/contact/tests/templates/base.html

Changelog
---------

1.3
...

* Put sender email in Reply-To instead of From.

1.2
...

* Responsive CSS layout.

1.1
...

* Update for Django 1.8 and later.

1.0
...

* Stable release.

0.3
...

* Refactored tests for Django 1.6.

0.2
...

* Bundled stylesheet.

0.1
...

* Initial public release, extracted from my private repository.
* Switched the implementation to class-based generic views.
* Added documentation (README file).
