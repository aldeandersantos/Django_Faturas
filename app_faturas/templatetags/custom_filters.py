from django import template

register = template.Library()

@register.filter(name='get_by_number')
def get_by_number(queryset, number):
    return queryset[number - 1]