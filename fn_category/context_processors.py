from functools import partial
from . import models


def fn_category(request):
    return {
        'fn_category': models.Category.hierarchical(),
        'fn_category_selected': [],
    }
