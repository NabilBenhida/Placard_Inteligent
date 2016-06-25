from django import template

import datetime

register = template.Library()

# Pour sortir une date d'un timestamp

@register.filter(name='timestamptodate')
def timestamptodate(value):
	return datetime.datetime.fromtimestamp(value)
