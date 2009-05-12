from fn_creole.templatetags.fn_creole import fn_creole
from django import template

register = template.Library()


register.filter('fn_markup', fn_creole)
