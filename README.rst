# django-th-search
Search Engine for Django Trigger Happy

Installation 
============

follow the installation process from `Haystack <http://django-haystack.readthedocs.org/>` _

settings.py 
===========

add the module th_search to the INSTALLED_APPS


.. code:: python

   INSTALLED_APPS = (
        ...
        'haystack',
        'th_search',


urls.py
=======

add the following to your urls.py :


.. code:: python

    url(r'^th/search/', include('th_search.urls')),


update search 
=============

then let's index the search engine


.. code:: system

    python mange.py rebuild_search