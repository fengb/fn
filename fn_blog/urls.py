from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^blogs/$', views.blog_list),
    url(r'^blogs/(\d*)/$', views.blog),

    url(r'^entries/(\d*)/$', views.entry),
)
