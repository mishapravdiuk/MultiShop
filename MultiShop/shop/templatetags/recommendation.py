from django import template
from shop.models import *

register = template.Library()

@register.inclusion_tag('shop/recommendation.html')
def recommended_products():
    products = ProductInfo.objects.all()
    return {"products": products}