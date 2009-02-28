from . import models

def fn_styles(request):
    return {'fn_styles': models.Style.for_url(request.path)}
