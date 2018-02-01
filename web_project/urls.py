"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website.views import *

urlpatterns = [
    url(r'^Error404/', Error404.as_view(), name='e404'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^Ad/', Ad.as_view(), name='Ad'),
    url(r'^base/', Base.as_view(), name='base'),
    url(r'^blog_details/', Blog_details.as_view(), name='blog_details'),
    url(r'^blog_full_width/', Blog_full_width.as_view(), name='blog_full_width'),
    url(r'^blog_left_sidebar/', Blog_left_sidebar.as_view(), name='blog_left_sidebar'),
    url(r'^blog/', Blog.as_view(), name='blog'),
    url(r'^category/', Category.as_view(), name='category'),
    url(r'^checkout/', Checkout.as_view(), name='checkout'),
    url(r'^compare/', Compare.as_view(), name='compare'),
    url(r'^contact/', Contact.as_view(), name='contact'),
    url(r'^faq/', Faq.as_view(), name='faq'),
    url(r'^index_2/', Index_2.as_view(), name='index_2'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^login_form/', Login_form.as_view(), name='login_form'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^order/', Order.as_view(), name='order'),
    url(r'^product_details/', Product_details.as_view(), name='product_details'),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^seller/', Seller.as_view(), name='seller'),
    url(r'^services/', Services.as_view(), name='services'),
    url(r'^shop_grid/', Shop_grid.as_view(), name='shop_grid'),
    url(r'^shop_list/', Shop_list.as_view(), name='shop_list'),
    url(r'^shop_right_sidebar/', Shop_right_sidebar.as_view(), name='shop_right_sidebar'),
    url(r'^shop/', Shop.as_view(), name='shop'),
    url(r'^shopping_cart/', Shopping_cart.as_view(), name='shopping_cart'),
    url(r'^team/', Team.as_view(), name='team'),
    url(r'^wishlist/', Wishlist.as_view(), name='wishlist'),

    url(r'^', Index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]
