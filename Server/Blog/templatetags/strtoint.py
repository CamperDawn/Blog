from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def conv(value):
    """
    toma un string y lo transforma a entero
    """
    return int(value)