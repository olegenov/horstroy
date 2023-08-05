from django import template

register = template.Library()

@register.filter
def is_portrait(image):
    return image.height > image.width
