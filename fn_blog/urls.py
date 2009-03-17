from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.blog_list),
    url(r'^(\d*)/$', views.blog),

    url(r'^entries/(\d*)/$', views.entry),
)
