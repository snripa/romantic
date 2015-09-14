# coding=utf-8

from django.conf.urls import patterns, url, include
from party.views import PartyListView, PartyDetailView

urlpatterns = patterns('party.views',
    url(r'^party/$', PartyListView.as_view()),
    url(r'^party/(?P<pk>\d+)/$', PartyDetailView.as_view()),
    url(r'^party_new/$', 'party_new'),
)
