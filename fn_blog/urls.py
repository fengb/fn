from django.conf.urls.defaults import patterns, url
import fn_rest

from .views import blog, entry


urlpatterns = patterns('',
    #url(r'^blogs/', fn_rest.dispatch(blog)),
    #url(r'^entries/', fn_rest.dispatch(entry)),
)

urlpatterns += fn_rest.patterns(r'^blogs/', blog, 'fn_blog.blog')
urlpatterns += fn_rest.patterns(r'^entries/', entry, 'fn_blog.entry')
