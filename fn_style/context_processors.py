from . import models

def fn_style(request):
    return {'fn_style': models.Style.all_from_url(request.path)}
