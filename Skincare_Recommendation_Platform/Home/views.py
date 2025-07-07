from django.shortcuts import render

from Products.models import Product
# Create your views here.

def Home(request):
    Products = Product.objects.all()
    return render(request, 'Home/Home.html', {'products': list(Products)})