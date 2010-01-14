from . import models

def fn_link(request):
    return {'fn_link': models.Link.all_for_owners()}
