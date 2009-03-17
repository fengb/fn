from django.shortcuts import render_to_response
from django.template import RequestContext

from . import models


def category(request, id):
    vars = {}
    vars['category'] = category = models.Category.objects.get(id=int(id))

    return render_to_response('fn_category/category.html', vars,
                              context_instance=RequestContext(request))
