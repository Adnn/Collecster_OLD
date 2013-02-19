from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
 #   url(r'^releases/$', 'Datamanager.views.release_list'),
    url(r'^instance/add/(?P<release_id>\d+)/$', 'Datamanager.views.add_instance'),
    url(r'^instance/print/(?P<instance_id>\d+)/$', 'Datamanager.views.print_instance'),
) 

