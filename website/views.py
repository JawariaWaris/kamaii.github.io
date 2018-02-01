
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

class Error404(View):
    def get(self,request):
        return render(request,'404.html')

class About(View):
    def get(self,request):
        return render(request,'about.html')

class Ad(View):
    def get(self,request):
        return render(request,'Ad.html')

class Base(View):
    def get(self,request):
        return render(request, '../assets/../templates/base.html')

class Blog_details(View):
    def get(self,request):
        return render(request,'blog-details.html')

class Blog_full_width(View):
    def get(self,request):
        return render(request,'blog-full-width.html')

class Blog_left_sidebar(View):
    def get(self,request):
        return render(request,'blog-left-sidebar.html')

class Blog(View):
    def get(self,request):
        return render(request,'blog.html')

class Category(View):
    def get(self,request):
        return render(request,'category.html')

class Checkout(View):
    def get(self,request):
        return render(request,'checkout.html')

class Compare(View):
    def get(self,request):
        return render(request,'compare.html')

class Contact(View):
    def get(self,request):
        return render(request,'contact.html')

class Faq(View):
    def get(self,request):
        return render(request,'faq.html')

class Index_2(View):
    def get(self,request):
        return render(request,'index-2.html')

class Index(View):
    def get(self,request):
        return render(request,'index.html')

class Login_form(View):
    def get(self,request):
        return render(request,'login-form.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html')

class Order(View):
    def get(self,request):
        return render(request,'order.html')

class Product_details(View):
    def get(self,request):
        return render(request,'product-details.html')

class Register(View):
    def get(self,request):
        return render(request,'register.html')

class Seller(View):
    def get(self,request):
        return render(request,'seller.html')

class Services(View):
    def get(self,request):
        return render(request,'services.html')

class Shop_grid(View):
    def get(self,request):
        return render(request,'shop-grid.html')

class Shop_list(View):
    def get(self,request):
        return render(request,'shop-list.html')

class Shop_right_sidebar(View):
    def get(self,request):
        return render(request,'shop-right-sidebar.html')

class Shop(View):
    def get(self,request):
        return render(request,'shop.html')

class Shopping_cart(View):
    def get(self,request):
        return render(request,'shopping-cart.html')

class Team(View):
    def get(self,request):
        return render(request,'team.html')

class Urls(View):
    def get(self,request):
        return render(request,'urls.html')

class Views(View):
    def get(self,request):
        return render(request,'views.html')

class Wishlist(View):
    def get(self,request):
        return render(request,'wishlist.html')

