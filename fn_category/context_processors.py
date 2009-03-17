from . import models


def fn_category(request):
    return {
        'fn_category': models.Category.hierarchical(),
        'fn_category_view': 'fn_category.views.category',
        'fn_category_selected': set([]),
    }
