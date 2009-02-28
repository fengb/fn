from django.http import HttpResponse

from . import models


def style(request, id):
    style = models.Style.objects.get(id=int(id))
    return HttpResponse(style.body, mimetype='text/css')
