from pickle import loads
from django import template
register= template.Library()

@register.simple_tag
def load_data(data):
    return loads(data)
