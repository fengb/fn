from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

import fn_rest

from . import models
from . import forms


class Blogs(object):
    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blogs'] = models.Blog.objects.all()
        return render_to_response('fn_blog/blogs.html', vars)

    @login_required
    @fn_rest.method
    def post(self, request):
        blog = forms.Blog(request.POST).save()
        return HttpResponseRedirect(blog.get_absolute_url())

@login_required
@fn_rest.method('GET')
def blog_new(request):
    vars = {}
    vars['form'] = forms.Blog()
    return render_to_response('fn_blog/blog_new.html', vars)

class Blog(object):
    def __init__(self, id):
        self.resource = models.Blog.objects.get(id=int(id))

    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blog'] = self.resource
        vars['entries'] = self.resource.entry_set.all()
        return render_to_response('fn_blog/blog.html', vars)


class Entries(object):
    @login_required
    @fn_rest.method
    def post(self, request):
        entry = forms.Entry(request.POST).save()
        return HttpResponseRedirect(entry.get_absolute_url())

@login_required
@fn_rest.method('GET')
def entry_new(request):
    vars = {}
    vars['form'] = forms.Entry()
    return render_to_response('fn_blog/entry_new.html', vars)

class Entry(object):
    def __init__(self, id):
        self.resource = models.Entry.objects.get(id=int(id))

    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blog'] = self.resource.blog
        vars['entry'] = self.resource
        return render_to_response('fn_blog/entry.html', vars)
