from django.shortcuts import render_to_response
from django.template import RequestContext


def direct(request, page):
    return render_to_response('fn_direct/' + page, {},
                              context_instance=RequestContext(request))
