from django import template
from xbox.models import *

register = template.Library()

@register.filter
def to_and(value):
    return value.replace("...","")