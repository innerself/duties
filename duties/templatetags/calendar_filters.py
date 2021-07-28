import calendar

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def month_name(month_num: int) -> str:
    return calendar.month_name[month_num]


@register.filter
def nbsp(value: str) -> str:
    return mark_safe('&nbsp'.join(value.split(' ')))
