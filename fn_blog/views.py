from django.shortcuts import render_to_response
from django.template import RequestContext

from . import models


def blog_list(request):
    vars = {}
    vars['blogs'] = models.Blog.objects.all()
    vars['entries'] = models.Entry.objects.filter(public=True).order_by('-created')
    return render_to_response('fn_blog/blog_list.html', vars,
                             context_instance=RequestContext(request))


def blog(request, id):
    vars = {}
    vars['blog'] = blog = models.Blog.objects.get(id=int(id))

    #TODO: Push down into model
    if request.user == blog.owner:
        vars['entries'] = blog.entry_set.order_by('-created')
    else:
        vars['entries'] = blog.entry_set.filter(public=True).order_by('-created')

    return render_to_response('fn_blog/blog.html', vars,
                             context_instance=RequestContext(request))


def entry(request, id):
    vars = {}
    vars['entry'] = entry = models.Entry.objects.get(id=int(id))
    vars['blog'] = blog = entry.blog
    return render_to_response('fn_blog/entry.html', vars,
                             context_instance=RequestContext(request))
