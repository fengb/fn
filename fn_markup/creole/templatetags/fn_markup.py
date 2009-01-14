from creoleparser import creole_to_xhtml as render
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def fn_markup(string):
    return mark_safe(render(string))
