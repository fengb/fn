from . import models

def fn_styles(request):
    return {'fn_styles': models.Url.styles(request.path)}
