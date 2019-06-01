from django import template

register = template.Library()


@register.filter
def modulus(value):
    return value % 10
