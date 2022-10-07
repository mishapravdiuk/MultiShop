from ctypes import sizeof
from distutils.command.upload import upload
from email.policy import default
from platform import release
from statistics import quantiles
from tabnanny import verbose
from turtle import color
from unicodedata import category, name
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

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
    size=models.ManyToManyField(Size, related_name="product", blank=True)
    color=models.CharField(max_length=255, blank=True)
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
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering=['-created_at']

class ProductImage(models.Model):
    product=models.ForeignKey(ProductInfo, on_delete=models.CASCADE, default=None)
    image=models.ImageField(upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        db_table = 'Cart'
    
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product 