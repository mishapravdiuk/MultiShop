from email.policy import HTTP
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def get_category(request, slug):
    return render(request, 'shop/index.html')
