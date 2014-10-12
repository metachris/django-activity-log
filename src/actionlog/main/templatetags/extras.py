from django import template

register = template.Library()

def getPercent(value, value_total, result_max=100):
    return result_max / value_total * value

register.filter('getPercent', getPercent)
