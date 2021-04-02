"""shoppingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

app_name="ecomapp"
urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("about/",AboutView.as_view(),name="about"),
    path("contact-us/",ContactView.as_view(),name="contact"),
    path("all-products/",AllProductsView.as_view(),name="allproducts"),
    path("product/<slug:slug>/",ProductDetailView.as_view(),name="productdetail"),
    path("add-to-cart-<int:pro_id>/",AddToCartView.as_view(),name="addtocart"),
    path("my-cart/",MyCartView.as_view(),name="mycart"),
    path("manage.cart/<int:cp_id>/",ManageCartView.as_view(),name="managecart"),
    path("empty-cart/",EmptyCartView.as_view(),name="emptycart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
    path("register/",CustomerRegistrationView.as_view(),name="customerregistration"),
    path("logout/",CustomerLogoutView.as_view(),name="customerlogout"),
    path("login/",CustomerLoginView.as_view(),name="customerlogin"),
    path("profile/",CustomerProfileView.as_view(),name="customerprofile"),
    path("profile/order-<int:pk>/",CustomerOrderDetailView.as_view(),name="customerorderdetail"),
    path("admin-login/",AdminLoginView.as_view(),name="adminlogin"),
    path("admin-home/",AdminHomeView.as_view(),name="adminhome"),
    path("admin-order/<int:pk>/",AdminOrderDetailView.as_view(),name="adminorderdetail"),
    path("admin-all-order", AdminOrderListView.as_view(), name="adminorderlist"),
    path("admin-order-<int:pk>-change/",AdminOrderStatusChangeView.as_view(),name="adminorderstatuschange"),
    path("search/",SearchView.as_view(),name="search"),
    path("admin-product/list/",AdminProductListView.as_view(),name="adminproductlist"),
    path("admin-product/add/",AdminProductCreateView.as_view(),name="adminproductcreate"),


]
