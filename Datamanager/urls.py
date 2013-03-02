from django.conf.urls import patterns, include, url

from django.contrib import admin

from Datamanager.settings import *

admin.autodiscover()

urlpatterns = patterns('',
 #   url(r'^releases/$', 'Datamanager.views.release_list'),
    url(r'^'+URL_ADD_INSTANCE+'(?P<release_id>\d+)/$', 'Datamanager.views.add_instance'),
    url(r'^'+URL_PRINT_INSTANCE+'(?P<instance_id>\d+)/$', 'Datamanager.views.print_instance'),
) 

