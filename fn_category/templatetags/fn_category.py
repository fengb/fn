from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def contains(value, arg):
    return arg in value


@register.filter
def link(value, arg):
    """Naive link tag. Requires value to be a partial.

    Example: func_var|link:1
    """
    view = '%s.%s' % (value.func.__module__, value.func.__name__)
    if value.keywords:
        kwargs = {'category_id': arg}
        kwargs.update(value.keywords)
        return mark_safe(reverse(view, kwargs=kwargs))
    else:
        args = list(value.args)
        args.append(arg)
        return mark_safe(reverse(view, args=args))
