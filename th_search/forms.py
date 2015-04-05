# -*- coding: utf-8 -*-
from django import forms
from haystack.forms import SearchForm

class TriggerHappySearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
