from django.shortcuts import render

from Products.models import Product
# Create your views here.

def HomePage(request):
    
    # ----=== test search logic ===----
    # ---== temporarily here ==---
    # searched_text = request.GET.get('search')
    # if(searched_text):
    #     products = Product.objects.filter(name__icontains=searched_text)
    # else:
    #     products = Product.objects.all()  


    # ----=== add search logic here ===----






    products = Product.objects.all()


    return render(request, 'Home/Home.html', {'products': list(products)})