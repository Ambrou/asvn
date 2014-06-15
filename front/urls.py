#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('front.views',
    url(r'^creerdepot/$', 'creerDepot'),
)