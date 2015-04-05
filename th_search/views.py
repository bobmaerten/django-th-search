# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

from th_search.forms import TriggerHappySearchForm


def notes(request):
    form = TriggerHappySearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})
