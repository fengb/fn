from django import template
register = template.Library()


@register.filter
def fn_markup(string):
    return string
