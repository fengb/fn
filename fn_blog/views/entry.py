from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

import fn_rest

from fn_blog import models
from fn_blog import forms


render = fn_rest.renderer('fn_blog/entry')

#@fn_rest.collection
class Collection(object):
    fn_rest_suffix = '$'
    fn_rest_resource = '__collection__'

    @login_required
    @fn_rest.method
    def post(self, request):
        entry = forms.Entry(request.POST).save()
        return HttpResponseRedirect(entry.get_absolute_url())
Collection = fn_rest.collection(Collection)


#@fn_rest.member
class Member(object):
    fn_rest_suffix = r'(\d*)/$'
    fn_rest_resource = '__member__'

    def __init__(self, id):
        self.resource = models.Entry.objects.get(id=int(id))

    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['blog'] = self.resource.blog
        vars['entry'] = self.resource
        if request.user == vars['blog'].owner:
            vars['form'] = forms.Entry(instance=self.resource)
        return render(self, request, vars)
Member = fn_rest.member(Member)


#@fn_rest.cresource
class New(object):
    @login_required
    @fn_rest.method
    def get(self, request):
        vars = {}
        vars['form'] = forms.Entry()
        return render(self, request, vars)
New = fn_rest.cresource(New)
