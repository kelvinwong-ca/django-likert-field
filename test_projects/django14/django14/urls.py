# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',  # NOQA
    url(r'^$', TemplateView.as_view(template_name='app/home.html'),
        name='home'),
    url(r'^surveys/', include('likert_test_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
