from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def contains(value, arg):
    return arg in value


@register.filter
def link(value, arg):
    """Very simple and naive link tag.

    Example: 'app.views.func'|link:1
    """
    return mark_safe(reverse(value, args=[arg]))
