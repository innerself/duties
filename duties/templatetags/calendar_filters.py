import calendar

from django import template

register = template.Library()


@register.filter
def month_name(month_num: int) -> str:
    return calendar.month_name[month_num]
