from django import template
from shop.models import *

register = template.Library()

@register.inclusion_tag('shop/show_category.html')
def show_category():
    categories = Category.objects.all()
    return {"categories": categories}


@register.inclusion_tag('shop/category_view.html')
def category_view():
    categories = Category.objects.all()
    return {"categories": categories}

@register.inclusion_tag('shop/featured_products.html')
def featured_products():
    products = ProductInfo.objects.all()
    return {"products": products}