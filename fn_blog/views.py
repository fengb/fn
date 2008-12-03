from django.shortcuts import render_to_response
from fn_rest import method

from . import models


class Blogs(object):
    def __init__(self):
        self.resource = models.Blog.objects.all()

    @method
    def get(self, request):
        vars = {}
        vars['blogs'] = self.resource
        return render_to_response('fn_blog/blogs.html', vars)


class Blog(object):
    def __init__(self, id):
        self.resource = models.Blog.objects.get(id=int(id))

    @method
    def get(self, request):
        vars = {}
        vars['blog'] = self.resource
        vars['entries'] = self.resource.entry_set.all()
        return render_to_response('fn_blog/blog.html', vars)


class Entry(object):
    def __init__(self, id):
        self.resource = models.Entry.objects.get(id=int(id))

    @method
    def get(self, request):
        vars = {}
        vars['blog'] = self.resource.blog
        vars['entry'] = self.resource
        return render_to_response('fn_blog/entry.html', vars)
