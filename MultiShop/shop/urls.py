from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('store/', GetStore.as_view(), name='store'),
    path('category/<str:slug>/', ProductByCategory.as_view(), name='category'),
    path('product/<str:slug>/', GetProduct.as_view(), name='product'),
    path('search/', Search.as_view(), name='search'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', cart_remove_product, name='cart_remove_product'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add-product/', add_product, name='add_product'),
]