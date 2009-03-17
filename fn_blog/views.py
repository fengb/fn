from functools import partial
from django.shortcuts import render_to_response
from django.template import RequestContext

from . import models


def blog_list(request):
    vars = {}
    vars['blogs'] = models.Blog.objects.all()

    return render_to_response('fn_blog/blog_list.html', vars,
                              context_instance=RequestContext(request))


def blog(request, id, category_id=None):
    vars = {}
    vars['blog'] = blog = models.Blog.objects.get(id=int(id))
    vars['entries'] = blog.entries_by_user(request.user)
    vars['fn_category_view'] = partial(blog_view, id=blog.id)

    if category_id:
        category = models.Category.objects.get(id=int(category_id))
        vars['entries'] = vars['entries'].filter(categories=category)
        vars['fn_category_selected'] = [category]

    return render_to_response('fn_blog/blog.html', vars,
                              context_instance=RequestContext(request))
blog_view = blog


def entry(request, id):
    entry = models.Entry.objects.get(id=int(id))

    vars = {}
    vars['entry'] = entry
    vars['blog'] = blog = entry.blog
    vars['fn_category_view'] = partial(blog_view, id=blog.id)
    vars['fn_category_selected'] = set(entry.categories.iterator())
    return render_to_response('fn_blog/entry.html', vars,
                              context_instance=RequestContext(request))
