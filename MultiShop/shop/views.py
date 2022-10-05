from email.policy import HTTP
import re
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .forms import CreateUserForm
from .models import *
from django.db.models import F
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def get_category(request, slug):
    return render(request, 'shop/index.html')


class Home(ListView):
    model = ProductInfo
    template_name ='shop/index.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductByCategory(ListView):
    template_name = 'shop/store.html'
    context_object_name = 'product'
    # paginate_by = 9
    # allow_empty = False

    def get_queryset(self):
        return ProductInfo.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetProduct(DetailView):
    model = ProductInfo
    template_name = 'shop/product.html'
    context_object_name = 'product'
    paginate_by=4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class GetStore(ListView):
    model = ProductInfo
    template_name= 'shop/store.html'
    context_object_name = 'product'
    paginate_by=6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Search(ListView):
    template_name= 'shop/store.html'   
    context_object_name = 'product'  
    paginate_by=6

    def get_queryset(self):
        return ProductInfo.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&"
        return context



# class Cart(ListView):
#     model = CartItem
#     template_name='shop/cart.html'
#     context_object_name = 'product'


#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = ProductInfo.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.quantity:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    return redirect('cart_detail')



def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'shop/cart.html', dict(cart_items=cart_items, total=total, counter=counter))




def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(ProductInfo, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(ProductInfo, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


@csrf_exempt
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            messages.success(request, "You've registered successfully ")
            return redirect('login')
        else:
            messages.error(request, "Registration error")
    else:
        form = CreateUserForm()
    return render(request, 'shop/reg.html', {'form': form})




def logInPage(request):
    pass




