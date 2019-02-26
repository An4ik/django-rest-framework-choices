=====
Usage
=====

To use django-rest-framework-choices in a project, add it to your `INSTALLED_APPS`:

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
