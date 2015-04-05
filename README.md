# django-th-search
Search Engine for Django Trigger Happy

Installation 
============

follow the installation process from `Haystack <http://django-haystack.readthedocs.org/>`

settings.py 
===========

add the module th_search to the INSTALLED_APPS


.. code:: python

   INSTALLED_APPS = (
        ...
        'th_search',


.. code:: system

    python manage.py syncdb


then let's index the search engine

.. code:: system

    python mange.py rebuild_search