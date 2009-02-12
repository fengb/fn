from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

import fn_rest

from fn_blog import models
from fn_blog import forms


#@fn_rest.collection
class Collection(object):
    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blogs'] = models.Blog.objects.all()
        vars['entries'] = models.Entry.objects.filter(public=True).order_by('-created')
        return fn_rest.render(self, request, vars)

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
        if request.user == self.resource.owner:
            vars['entries'] = self.resource.entry_set.order_by('-created')
        else:
            vars['entries'] = self.resource.entry_set.filter(public=True).order_by('-created')

        return fn_rest.render(self, request, vars)
Member = fn_rest.member(Member)


#@fn_rest.cresource
class New(object):
    @login_required
    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['form'] = forms.Blog()
        return fn_rest.render(self, request, vars)
New = fn_rest.cresource(New)
