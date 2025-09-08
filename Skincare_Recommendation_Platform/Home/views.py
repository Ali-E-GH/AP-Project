from django.shortcuts import render

from Products.models import Product
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

def HomePage(request):
    
    products = Product.objects.all()


    return render(request, 'Home/Home.html', {'products': list(products)})
