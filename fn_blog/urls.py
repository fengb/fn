from django.conf.urls.defaults import patterns, url
from . import views

urlpatterns = patterns('',
     url(r'^$', views.list_blogs),
     url(r'^(\w+)$', views.show_blog),
     url(r'^(\w+)/(\w+)$', views.show_entry),
)
