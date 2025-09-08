from django.shortcuts import render, get_object_or_404
from statistics import mean
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q, TextField
from django.db.models.functions import Cast

from .models import Product
from History.models import Browsing_History
# Create your views here.

def SearchProducts(request):
    pass


def ProductPage(request, id):
    product = get_object_or_404(Product, id=id)
    ingredients = [ing.replace('_', ' ') for ing in list(product.ingredients)]

    # Browsing_History.objects.create(user=request.user, product=product, interaction_type='view')
    if(request.user.is_authenticated):
        object_query = Browsing_History.objects.filter(user=request.user, product=product, interaction_type='like')
        already_liked = object_query.exists()
    else:
        already_liked = False

    if(request.POST.get('user_rating')):
        ratings = product.ratings
        ratings.append(float(request.POST.get('user_rating')))
        product.ratings = ratings
        product.save()




    return render(request, 'Products/product_page.html', {
        'product': product,
        'ingredients':ingredients,
        'last_ingredient':ingredients[-1] if ingredients else None,
        'rating': product.rating,
        'liked': already_liked,
        'views':Browsing_History.objects.filter(product=product, interaction_type='view').count(),
    })

def SearchPage(request):
    if(request.method == 'POST'):
        query = request.POST.get('search', '').strip()
        products = Product.objects.all()

        if query:
            vector = (
                SearchVector('name', weight='A') +
                SearchVector('brand', weight='A') +
                SearchVector('category', weight='A') +
                SearchVector('description', weight='B') +
                SearchVector(Cast('compatible_skin_types', TextField()), weight='B') +
                SearchVector(Cast('concerns_targeted', TextField()), weight='B') +
                SearchVector(Cast('ingredients', TextField()), weight='B') +
                SearchVector(Cast('tags', TextField()), weight='C') +
                SearchVector('rating_avg', weight='B')
            )

            search_query = SearchQuery(query)

            products = (
                Product.objects.annotate(rank=SearchRank(vector, search_query))
                .filter(rank__gte=0.1)
                .order_by('-rank')
            )

            if not products.exists():
                products = Product.objects.filter(
                    Q(name__icontains=query) |
                    Q(brand__icontains=query) |
                    Q(category__icontains=query) |
                    Q(description__icontains=query) |
                    Q(compatible_skin_types__icontains=query) |
                    Q(concerns_targeted__icontains=query) |
                    Q(ingredients__icontains=query) |
                    Q(tags__icontains=query)
                )

    elif(request.method == 'GET'):
        brand_name = request.GET.get('brand_filter')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        min_rating = request.GET.get('min_rating')
        max_rating = request.GET.get('max_rating')
        category = request.GET.get('category_filter')
        skin_types = request.GET.getlist('skin_type_options')
        concerns = request.GET.getlist('targeted_concerns_options')
        ingredients = request.GET.getlist('ingredients_options')
        #rest here
        query = request.GET.get('searched_phrase', '').strip()
        products = Product.objects.all()

        if query:
            vector = (
                SearchVector('name', weight='A') +
                SearchVector('brand', weight='A') +
                SearchVector('category', weight='A') +
                SearchVector('description', weight='B') +
                SearchVector(Cast('compatible_skin_types', TextField()), weight='B') +
                SearchVector(Cast('concerns_targeted', TextField()), weight='B') +
                SearchVector(Cast('ingredients', TextField()), weight='B') +
                SearchVector(Cast('tags', TextField()), weight='C') +
                SearchVector('rating_avg', weight='B')
            )

            search_query = SearchQuery(query)

            products = (
                Product.objects.annotate(rank=SearchRank(vector, search_query))
                .filter(rank__gte=0.1)
                .order_by('-rank')
            )

            if not products.exists():
                products = Product.objects.filter(
                    Q(name__icontains=query) |
                    Q(brand__icontains=query) |
                    Q(category__icontains=query) |
                    Q(description__icontains=query) |
                    Q(compatible_skin_types__icontains=query) |
                    Q(concerns_targeted__icontains=query) |
                    Q(ingredients__icontains=query) |
                    Q(tags__icontains=query)
                )
        if(brand_name):
            products = products.filter(brand=brand_name)
        if(category):
            products = products.filter(category=category)
        if(skin_types):
            products = products.filter(compatible_skin_types__overlap=skin_types)
        if(concerns):
            products = products.filter(concerns_targeted__overlap=concerns)
        if(ingredients):
            products = products.filter(ingredients__overlap=ingredients)
        if(min_price and max_price):
            products = products.filter(price__gte=min_price, price__lte=max_price)
        elif(min_price):
            products = products.filter(price__gte=min_price)
        elif(max_price):
            products = products.filter(price__lte=max_price)
        if(min_rating and max_rating):
            products = products.filter(rating_avg__gte=min_rating, rating_avg__lte=max_rating)
        elif(min_rating):
            products = products.filter(rating_avg__gte=min_rating)
        elif(max_rating):
            products = products.filter(rating_avg__lte=max_rating)


    return render(request, 'Products/search_page.html', {
        'products': products,
        'searched': query
    })