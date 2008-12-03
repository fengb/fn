from django.http import Http404, HttpResponseNotAllowed
from django.core.exceptions import ObjectDoesNotExist


def method(func):
    func.is_method = True
    return func


class Dispatch(object):
    def __init__(self, resource_class):
        self.resource_class = resource_class
        self.supported = {}

        for name in dir(resource_class):
            try:
                attribute = getattr(resource_class, name)
                if attribute.is_method:
                    self.supported[name.upper()] = attribute
            except AttributeError:
                pass

    def __call__(self, request, *args, **kwargs):
        if request.method not in self.supported:
            return HttpResponseNotAllowed(self.supported.keys())
        else:
            try:
                resource = self.resource_class(*args, **kwargs)
                return self.supported[request.method](resource, request)
            except ObjectDoesNotExist:
                raise Http404
