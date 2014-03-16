#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

#from .forms import SurveyForm
from .models import ParametersModel


class SurveyListView(ListView):
    context_object_name = 'surveys'
    model = ParametersModel
    template_name = 'likert/index.html'


class SurveyCreateView(CreateView):
    model = ParametersModel
    #fields = ['item', 'another_item']
    #form_class = SurveyForm
    template_name = 'likert/add.html'
    success_url = reverse_lazy('likert_added')


class SurveyDetailView(DetailView):
    context_object_name = 'survey'
    model = ParametersModel
    template_name = 'likert/detail.html'
