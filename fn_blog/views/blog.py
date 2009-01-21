from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

import fn_rest

from fn_blog import models
from fn_blog import forms


render = fn_rest.renderer('fn_blog/blog')

#@fn_rest.collection
class Collection(object):
    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blogs'] = models.Blog.objects.all()
        return render(self, request, vars)

    @login_required
    @fn_rest.method
    def post(self, request):
        blog = forms.Blog(request.POST).save()
        return HttpResponseRedirect(blog.get_absolute_url())
Collection = fn_rest.collection(Collection)


#@fn_rest.member
class Member(object):
    def __init__(self, id):
        self.resource = models.Blog.objects.get(id=int(id))

    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blog'] = self.resource
        vars['entries'] = self.resource.entry_set.all()
        return render(self, request, vars)
Member = fn_rest.member(Member)


#@fn_rest.cresource
class New(object):
    @login_required
    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['form'] = forms.Blog()
        return render(self, request, vars)
New = fn_rest.cresource(New)
