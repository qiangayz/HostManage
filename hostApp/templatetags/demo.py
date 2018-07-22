from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def fun1(a1,a2,a3):
    return a1 + a2 +a3

@register.filter
def fun2(a1,a2):
    print(a2,type(a2))
    return a1 + str(a2)