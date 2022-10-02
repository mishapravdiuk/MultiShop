from django import template
from shop.models import *

register = template.Library()

@register.inclusion_tag('shop/recommendation.html')
def recommended_products(cnt=6):
    products = ProductInfo.objects.order_by('-views')[:cnt]
    return {"products": products}