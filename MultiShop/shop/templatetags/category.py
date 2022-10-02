from django import template
from shop.models import *

register = template.Library()

@register.inclusion_tag('shop/show_category.html')
def show_category():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag('shop/category_view.html')
def category_view(cnt=12):
    categories = Category.objects.all()[:cnt]
    return {"categories": categories}

@register.inclusion_tag('shop/featured_products.html')
def featured_products(cnt=8):
    products = ProductInfo.objects.order_by('-views')[:cnt]
    return {"products": products}