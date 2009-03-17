from functools import partial
from . import models, views


def fn_category(request):
    return {
        'fn_category': models.Category.hierarchical(),
        'fn_category_view': partial(views.category),
        'fn_category_selected': set([]),
    }
