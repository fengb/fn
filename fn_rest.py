from functools import partial

from django.http import Http404, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist
from django.conf.urls import defaults as django
from django.shortcuts import render_to_response


def _method_decorator(func, name):
    func.fn_rest_method = name
    return func

def method(name):
    if callable(name):
        return _method_decorator(name, name.__name__.upper())
    else:
        return partial(_method_decorator, name=name)


def _resource_decorator(cls, name, url):
    cls.fn_rest_name = name
    cls.fn_rest_url = url

    cls.fn_rest_methods = {}
    for name in dir(cls):
        try:
            attribute = getattr(cls, name)
            cls.fn_rest_methods[attribute.fn_rest_method] = name
        except AttributeError:
            pass

    return cls

def resource(name, url):
    return partial(_resource_decorator, name=name, url=url)

def cresource(obj):
    name = obj.__name__.lower()
    return _resource_decorator(obj, name, r'%s$' % name)

def mresource(obj):
    name = obj.__name__.lower()
    return _resource_decorator(obj, name, r'(\d)*/%s$' % name)

collection = resource('__collection__', '$')
member = resource('__member__', r'(\d*)/$')


def _invoke_method(cls, request, *args, **kwargs):
    if request.method not in cls.fn_rest_methods:
        return HttpResponseNotAllowed(self.supported.keys())
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
    return partial(_invoke, cls)

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

def render(directory, obj, request, vars):
    template = '%s/%s.%s' % (directory, obj.fn_rest_name, 'html')
    return render_to_response(template, vars)

def renderer(directory):
    return partial(render, directory)
