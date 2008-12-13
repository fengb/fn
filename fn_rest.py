from functools import partial

from django.http import Http404, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from django.conf.urls import defaults as django


"""
>>> import fn_rest

>>> class Resource(object):
...     def __init__(self, a, b):
...         self.a = a
...         self.b = b

...     @fn_rest.method
...     def get(self, request):
...         return (a, b)

...     @fn_rest.method('POST')
...     def subtract(self, request):
...         return a - b
...

>>> dr = fn_rest.dispatch(Resource)

>>> class Request(object):
...     def __init__(self, method):
...         self.method = method

>>> dr(Request('GET'))
(1, 2)

>>> dr(Request('POST'))
-1

>>> dr(Request('SUBTRACT'))
Traceback (most recent call last):
HttpResponseNotAllowed
"""


def _method_decorator(func, name):
    func.fn_rest_method = name
    return func

def method(arg):
    if callable(arg):
        return _method_decorator(arg, arg.__name__.upper())
    else:
        return partial(_method_decorator, name=arg)


def _resource_decorator(cls, name, url):
    cls.fn_rest_resource = name
    return cls

def resource(arg, url=None):
    if callable(arg):
        return _method_decorator(arg, arg.__name__.upper())
    elif url:
        return partial(_resource_decorator, name=arg, url=url)
    else:
        return partial(_resource_decorator, name=arg, url=arg)

def collection(cls):
    return _resource_decorator(cls, '__collection__')

def member(cls):
    return _resource_decorator(cls, '__member__')


class Dispatch(object):
    def __init__(self, resource_class):
        self.resource_class = resource_class
        self.supported = {}

        for name in dir(resource_class):
            try:
                attribute = getattr(resource_class, name)
                self.supported[attribute.fn_rest_method] = name
            except AttributeError:
                pass

    def __call__(self, request, *args, **kwargs):
        if request.method not in self.supported:
            return HttpResponseNotAllowed(self.supported.keys())
        else:
            try:
                resource = self.resource_class(*args, **kwargs)
                # Calling an unbound method upon the resource is the simplest
                # @login_required does not work with the unbound approach
                #return self.supported[request.method](resource, request)

                attr_name = self.supported[request.method]
                return getattr(resource, attr_name)(request)
            except ObjectDoesNotExist:
                raise Http404


def _gen_urls(base, module, namespace):
    for name in dir(module):
        attribute = getattr(module, name)
        try:
            url = base + attribute.fn_rest_suffix
            name = '.'.join([namespace, attribute.fn_rest_resource])

            yield django.url(url, Dispatch(attribute), name=name)
        except AttributeError:
            pass


def patterns(prefix, module, namespace):
    return django.patterns('', *_gen_urls(prefix, module, namespace))
