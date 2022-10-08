import re
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', help_text="Your name should contain not more then 150 characters", widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))

class ProductForm(forms.Form):
    title=forms.CharField(max_length=255, label="Product name", widget=forms.TextInput(attrs={"class": "form-control"}))
    slug=forms.SlugField(label="Product slug", max_length=255, widget=forms.TextInput(attrs={"class": "form-control"}))
    # size=forms.ModelMultipleChoiceField(queryset=Size.objects.all(), label="Product size", required=False)
    color=forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    category=forms.ModelChoiceField(queryset=Category.objects.all(), label="Product category", empty_label="Choose category", widget=forms.Select(attrs={"class": "form-control"}))
    price=forms.FloatField(label="Product price", widget=forms.NumberInput(attrs={"class": "form-control"}))
    description=forms.CharField(label="Product description", widget=forms.Textarea(attrs={"class": "form-control"}))
    # photo=forms.ImageField(required=False, label="Photo", widget=forms.ClearableFileInput(attrs={"multiple": "True"}))
    quantity=forms.IntegerField(label="Product quantity", widget=forms.NumberInput(attrs={"class": "form-control"}))


class ContactForm(forms.Form):
    user_name=forms.CharField(max_length=255, label="Your name", widget=forms.TextInput(attrs={"class": "form-control"}))
    subject=forms.CharField(max_length=255, label="Mail subject", widget=forms.TextInput(attrs={"class": "form-control"}))
    content=forms.CharField(max_length=255, label="Message", widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    user_mail=forms.CharField(max_length=255, label= "Your email", widget=forms.EmailInput(attrs={"class": "form-control", "rows": 5}))


