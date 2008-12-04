from functools import partial

from django.http import Http404, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist


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

>>> @fn_rest.method('PUT')
... def add(a, b):
...     return a + b
...
>>> function(1, 2)
3
>>> df = fn_rest.dispatch(add)
>>> df(Request('PUT')
3
>>> df(Request('GET')
Traceback (most recent call last):
HttpResponseNotAllowed
"""


def _method_decorator(func, name):
    func.fn_rest_method = name
    return func


def method(arg):
    if callable(arg):
        return _method_decorator(arg, arg.func_name.upper())
    else:
        return partial(_method_decorator, name=arg)


class DispatchClass(object):
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


class DispatchFunction(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, request, *args, **kwargs):
        if request.method != self.function.fn_rest_method:
            return HttpResponseNotAllowed([self.function.fn_rest_method])
        else:
            return self.function(request, *args, **kwargs)


def dispatch(arg):
    if hasattr(arg, 'fn_rest_method'):
        return DispatchFunction(arg)
    else:
        return DispatchClass(arg)
