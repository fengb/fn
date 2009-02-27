from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from . import models, forms


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


@login_required
def entry_new(request):
    vars = {}
    vars['form'] = forms.Entry()
    return render_to_response('fn_blog/entry_new.html', vars,
                             context_instance=RequestContext(request))


@login_required
def entry_list(request):
    if request.method == 'POST':
        entry = forms.Entry(request.POST).save()
        return HttpResponseRedirect(reverse('fn_blog.views.entry', args=[entry.id]))


def entry(request, id):
    entry = models.Entry.objects.get(id=int(id))
    if request.method == 'POST':
        entry = forms.Entry(request.POST, instance=entry).save()

    vars = {}
    vars['entry'] = entry
    vars['blog'] = blog = entry.blog
    if request.user == vars['blog'].owner:
        vars['form'] = forms.Entry(instance=entry)
    return render_to_response('fn_blog/entry.html', vars,
                             context_instance=RequestContext(request))
