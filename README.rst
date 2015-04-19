================
django-th-search
================
A Search Engine for Django Trigger Happy


Requirements
============
* `dango-haystack <https://github.com/django-haystack/django-haystack>`_ == 2.3.1
* `django_th <https://github.com/foxmask/django-th>`_ >= 0.10.0

Installation 
============

Haystack
--------

follow the installation process from `Haystack <http://django-haystack.readthedocs.org/>`_

settings.py 
-----------

add the module th_search to the INSTALLED_APPS


.. code:: python

   INSTALLED_APPS = (
        ...
        'haystack',
        'th_search',


urls.py
-------

add the following to your urls.py :


.. code:: python

    url(r'^th/search/', include('th_search.urls')),


update search 
-------------

then let's index the search engine


.. code:: system

    python mange.py rebuild_search
