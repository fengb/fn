from . import models

def fn_styles(request):
    return {'fn_styles': models.Style.all_from_url(request.path)}
