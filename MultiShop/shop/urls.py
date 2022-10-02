from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', ProductByCategory.as_view(), name='category'),
    path('product/<str:slug>/', GetProduct.as_view(), name='product'),
]