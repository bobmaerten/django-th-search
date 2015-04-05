from django.conf.urls import patterns, url
from haystack.query import SearchQuerySet
from th_search.forms import TriggerHappySearchForm
from th_search.views import TriggerHappySearchView

urlpatterns = \
	patterns('',
    	url(r'',
        	TriggerHappySearchView(
            	template='search.html',
            	searchqueryset=SearchQuerySet().all(),
            	form_class=TriggerHappySearchForm
            ),
         	name='my_search'
        ),
    )
