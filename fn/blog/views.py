from django.shortcuts import render_to_response

from .models import User, Blog


def show_root(request):
    vars = {}
    vars['blogs'] = Blog.objects.all()
    return render_to_response('fn/blog/show_root.html', vars)


def show_blog(request, username):
    vars = {}
    vars['owner'] = owner = User.objects.get(username=username)
    vars['blog'] = blog = Blog.objects.get(owner=owner)
    vars['entries'] = blog.entry_set.all()
    return render_to_response('fn/blog/show_blog.html', vars)


def show_entry(request, username, entry_internal):
    vars = {}
    vars['owner'] = owner = User.objects.get(username=username)
    vars['blog'] = blog = Blog.objects.get(owner=owner)
    vars['entry'] = blog.entry_set.get(internal=entry_internal)
    return render_to_response('fn/blog/show_entry.html', vars)
