from django.conf.urls.defaults import patterns, url
import fn_rest

from . import views

urlpatterns = patterns('',
     url(r'^blogs/$', fn_rest.dispatch(views.Blogs),
                      name='fn_blog.blogs'),
     url(r'^blogs/new/$', fn_rest.dispatch(views.blog_new),
                          name='fn_blog.blog_new'),
     url(r'^blogs/(\d*)/$', fn_rest.dispatch(views.Blog),
                            name='fn_blog.blog'),

     url(r'^entries/$', fn_rest.dispatch(views.Entries),
                        name='fn_blog.entries'),
     url(r'^entries/new/$', fn_rest.dispatch(views.entry_new),
                            name='fn_blog.entry_new'),
     url(r'^entries/(\d*)/$', fn_rest.dispatch(views.Entry),
                            name='fn_blog.entry'),
)
