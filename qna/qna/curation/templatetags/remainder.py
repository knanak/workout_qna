from django import template

register = template.Library()

@register.filter
def remainder(value, divisor):
    return value % divisor