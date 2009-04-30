from functools import partial
from django.shortcuts import render_to_response
from django.template import RequestContext

from . import models


def blog_list(request):
    blogs = models.Blog.objects.all()

    return render_to_response('fn_blog/blog_list.html', locals(),
                              context_instance=RequestContext(request))


def blog(request, id):
    blog = models.Blog.objects.get(id=int(id))
    entries = blog.entries_by_user(request.user)
    fn_category_view = partial(blog_category, blog.id)

    return render_to_response('fn_blog/blog.html', locals(),
                              context_instance=RequestContext(request))


def blog_category(request, id, category_id):
    blog = models.Blog.objects.get(id=int(id))
    category = models.Category.objects.get(id=int(category_id))
    entries = blog.entries_by_user(request.user).filter(categories=category)
    fn_category_view = partial(blog_category, blog.id)
    fn_category_selected = [category]

    return render_to_response('fn_blog/blog.html', locals(),
                              context_instance=RequestContext(request))


def entry(request, id):
    entry = models.Entry.objects.get(id=int(id))
    blog = entry.blog
    fn_category_view = partial(blog_category, blog.id)
    fn_category_selected = set(entry.categories.iterator())

    return render_to_response('fn_blog/entry.html', locals(),
                              context_instance=RequestContext(request))
