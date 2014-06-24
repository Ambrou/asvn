#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from front.views import AboutView

# urlpatterns = patterns('front.views',
    # url(r'^creerdepot/$', 'creerDepot'),
# )

urlpatterns = [
    url(r'^creerdepot/$', AboutView.as_view()),
]