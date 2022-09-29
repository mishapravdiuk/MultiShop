from ctypes import sizeof
from distutils.command.upload import upload
from platform import release
from tabnanny import verbose
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
    category=models.ForeignKey(Category, on_delete=models.PROTECT, related_name="product")
    price=models.FloatField()
    description=models.TextField()
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # reviews 
    # rating 
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=255, unique=True) 
    views = models.IntegerField(default=0, verbose_name='Number of views')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'