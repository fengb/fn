from functools import partial


def _method_decorator(func, name):
    func.fn_rest_method = name
    return func

def method(name):
    if callable(name):
        return _method_decorator(name, name.__name__.upper())
    else:
        return partial(_method_decorator, name=name)


def _resource_decorator(cls, name, url, target=None):
    cls.fn_rest_name = name
    cls.fn_rest_url = url

    app_name, sep, app_target = cls.__module__.partition('.views.')
    app_name = app_name.split('.')[-1]
    if not target:
        cls.fn_rest_target = '/'.join([app_name, app_target.replace('.', '/'), name])
    else:
        cls.fn_rest_target = '/'.join([app_name, target])

    cls.fn_rest_methods = {}
    for name in dir(cls):
        try:
            attribute = getattr(cls, name)
            cls.fn_rest_methods[attribute.fn_rest_method] = name
        except AttributeError:
            pass

    return cls

def resource(*args, **kwargs):
    return lambda cls: _resource_decorator(cls, *args, **kwargs)

def cresource(obj):
    name = obj.__name__.lower()
    return _resource_decorator(obj, name, r'%s$' % name)

def mresource(obj):
    name = obj.__name__.lower()
    return _resource_decorator(obj, name, r'(\d)*/%s$' % name)

collection = resource('__collection__', '$')
member = resource('__member__', r'(\d*)/$')
