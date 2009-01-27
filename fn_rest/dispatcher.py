from functools import partial

from django.http import Http404, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from django.conf.urls import defaults as django


def _invoke_method(cls, request, *args, **kwargs):
    if request.method not in cls.fn_rest_methods:
        return HttpResponseNotAllowed(cls.fn_rest_methods.keys())
    else:
        try:
            resource = cls(*args, **kwargs)
            # Calling an unbound method upon the resource is the simplest
            # @login_required does not work with the unbound approach
            #return cls.fn_rest_methods[request.method](resource, request)

            method_name = cls.fn_rest_methods[request.method]
            return getattr(resource, method_name)(request)
        except ObjectDoesNotExist:
            raise Http404

def dispatch(cls):
    return partial(_invoke_method, cls)


def _gen_urls(base, module, namespace):
    for name in dir(module):
        attribute = getattr(module, name)
        try:
            url = base + attribute.fn_rest_url
            name = '%s.%s' % (namespace, attribute.fn_rest_name)

            yield django.url(url, dispatch(attribute), name=name)
        except AttributeError:
            pass


def patterns(prefix, module, namespace):
    return django.patterns('', *_gen_urls(prefix, module, namespace))
