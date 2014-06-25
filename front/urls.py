#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from front.views import CreerDepotView


urlpatterns = [
    url(r'^creerdepot/$', CreerDepotView.as_view()),
]