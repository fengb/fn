from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.blog_list),
    url(r'^(\d*)/$', views.blog),
    url(r'^(\d*)/category/(\d*)/$', views.blog_category),
    url(r'^entry/(\d*)/$', views.entry),
)
