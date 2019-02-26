=============================
django-rest-framework-choices
=============================

.. image:: https://badge.fury.io/py/django-rest-framework-choices.svg
    :target: https://badge.fury.io/py/django-rest-framework-choices

.. image:: https://travis-ci.org/An4ik/django-rest-framework-choices.svg?branch=master
    :target: https://travis-ci.org/An4ik/django-rest-framework-choices

.. image:: https://codecov.io/gh/An4ik/django-rest-framework-choices/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/An4ik/django-rest-framework-choices

Your project description goes here

Documentation
-------------

The full documentation is at https://django-rest-framework-choices.readthedocs.io.

Quickstart
----------

Install django-rest-framework-choices::

    pip install django-rest-framework-choices

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_rest_framework_choices.apps.DjangoRestFrameworkChoicesConfig',
        ...
    )

Add django-rest-framework-choices's URL patterns:

.. code-block:: python

    from django_rest_framework_choices import urls as django_rest_framework_choices_urls


    urlpatterns = [
        ...
        url(r'^', include(django_rest_framework_choices_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
