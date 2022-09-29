from django import template
from shop.models import *

register = template.Library()

@register.inclusion_tag('shop/show_category.html')
def show_category():
    categories = Category.objects.all()
    return {"categories": categories}
