from django import forms
from .models import *
from django.contrib.auth.models import User


class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["ordered_by","shipping_address","mobile","email",]

class CustomerRegistrationForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())
    password= forms.CharField(widget=forms.PasswordInput())
    email= forms.CharField(widget=forms.EmailInput())

    class Meta:
        model= Customer
        fields=["username","password","email","full_name","address"]

    def clean_username(self):
        uname=self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists.")
        else:
            return uname

class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ProductForm(forms.ModelForm):
    more_images=forms.FileField(required=False,widget=forms.FileInput(attrs={
        "class":"form-control",
        "multiple":True
    }))
    class Meta:
        model=Product
        fields=["title","slug","category","image","marked_price","selling_price","description","warranty","return_policy"]
        widgets={
            "title":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter the product title here.."
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the unique slug here..."
            }),
            "category": forms.Select(attrs={
                "class": "form-control",
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "marked_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Marked price of the product here..."
            }),
            "selling_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Selling price of the product here..."
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description of the product here..."
            }),
            "warranty": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the warranty here.."
            }),
            "return_policy": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product return_policy here.."
            }),


        }

