from functools import partial

from django.template import TemplateDoesNotExist
from django.http import Http404
from django.core import serializers
from django.shortcuts import render_to_response as render_template


def map_types(request):
    #TODO: Actually parse the request accepted types
    return [('text/html', 'html')]


def render(directory, obj, request, vars):
    #TODO: Verify acceptable resource can be returned before running method
    accepts = map_types(request.META['HTTP_ACCEPT'])
    for mimetype, filetype in accepts:
        try:
            template = '%s/%s.%s' % (directory, obj.fn_rest_name, filetype)
            return render_template(template, vars, mimetype=mimetype)
        except TemplateDoesNotExist:
            #TODO: Attempt to render a serialized version
            pass
    #TODO: Use 406 instead
    raise Http404

def renderer(directory):
    return partial(render, directory)
