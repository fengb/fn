from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^blogs/$', views.blog_list),
    url(r'^blogs/(\d*)/$', views.blog),

    url(r'^entries/$', views.entry_list),
    url(r'^entries/new$', views.entry_new),
    url(r'^entries/(\d*)/$', views.entry),
)
