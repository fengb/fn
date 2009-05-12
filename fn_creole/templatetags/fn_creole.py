from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from creoleparser import creole_to_xhtml

register = template.Library()


@register.filter
@stringfilter
def fn_creole(string):
    return mark_safe(creole_to_xhtml(string))
