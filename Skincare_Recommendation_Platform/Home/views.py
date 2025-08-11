from django.shortcuts import render

from Products.models import Product
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

def HomePage(request):
    
    # ----=== test search logic ===----
    # ---== temporarily here ==---
    # searched_text = request.GET.get('search')
    # if(searched_text):
    #     products = Product.objects.filter(name__icontains=searched_text)
    # else:
    #     products = Product.objects.all()  


    # ----=== add search logic here ===----
    query = request.GET.get('search', '').strip()
    products = Product.objects.all()

    if query:

        vector = (
            SearchVector('name', weight='A') +
            SearchVector('brand', weight='A') +
            SearchVector('category', weight='A') +
            SearchVector('description', weight='B') +
            SearchVector('compatible_skin_types', weight='B') +
            SearchVector('rating', weight='B') +
            SearchVector('tags', weight='C')
        )

        search_query = SearchQuery(query)

        products = (Product.objects.annotate(rank=SearchRank(vector, search_query)).filter(rank__gte=0.1) .order_by('-rank').select_related('category'))


    if not products.exists():
        products = Product.objects.filter(Q(brand__icontains=query) | Q(category__name__icontains=query) | Q(description__icontains=query) | Q(compatible_skin_types__icontains=query) | Q(concerns_targeted__icontains=query) | Q(ingredients__icontains=query) | Q(tags__icontains=query))



    products = Product.objects.all()


    return render(request, 'Home/Home.html', {'products': list(products)})
