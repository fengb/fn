from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^(\S*)/(\d*)/([0-9a-fA-F]{6})/([^/]*)/$', views.texter),
    url(r'^(\S*)/(\d*)/([0-9a-fA-F]{6})/([^/]*)/(.*)/$', views.texter),
)
