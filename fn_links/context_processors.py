from . import models

def fn_links(request):
    return {'fn_links': models.Link.all_for_owners()}
