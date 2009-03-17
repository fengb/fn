from django.shortcuts import render_to_response
from django.template import RequestContext

from . import models


def category(request, id):
    category = models.Category.objects.get(id=int(id))

    vars = {}
    vars['category'] = category
    vars['fn_category_selected'] = [category]

    return render_to_response('fn_category/category.html', vars,
                              context_instance=RequestContext(request))
