from ctypes import sizeof
from platform import release
from turtle import color
from unicodedata import category, name
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Size(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Size'


class ProductInfo(models.Model):
    title=models.CharField(max_length=255)
    size=models.ManyToManyField(Size, related_name="product")
    color=models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    price=models.FloatField()
    description=models.TextField()
    photo=models.ImageField()
    # reviews 
    # rating 
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=255, unique=True) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'