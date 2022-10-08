from django import template
from shop.models import *
from django.shortcuts import render, get_object_or_404


register = template.Library()

@register.inclusion_tag('shop/get_images.html')
def get_image(id):
    product = get_object_or_404(ProductInfo, id=id)
    photos = ProductImage.objects.filter(product=product)
    return {'product': product, "photos": photos}