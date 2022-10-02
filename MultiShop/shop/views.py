from email.policy import HTTP
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

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
    template_name = 'shop/index.html'
    context_object_name = 'products'
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
    template_name = 'shop/index.html'
    context_object_name = 'product'
    paginate_by=4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context