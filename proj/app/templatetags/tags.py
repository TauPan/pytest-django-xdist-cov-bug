from django import template

register = template.Library()


@register.simple_tag
def add(args):
    return "The answer is {}.".format(sum([int(n) for n in args], 0))
