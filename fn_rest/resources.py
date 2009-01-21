from functools import partial


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
