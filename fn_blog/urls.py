from django.conf.urls.defaults import patterns, url
from fn_rest import Dispatch

from . import views

urlpatterns = patterns('',
     url(r'^blogs$', Dispatch(views.Blogs), name='fn_blog.blogs'),
     url(r'^blogs/(\d*)$', Dispatch(views.Blog), name='fn_blog.blog'),
     url(r'^entries/(\d*)$', Dispatch(views.Entry), name='fn_blog.entry'),
)
