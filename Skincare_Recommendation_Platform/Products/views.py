from django.shortcuts import render, get_object_or_404
from statistics import mean

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
        product.ratings.append(float(request.POST.get('user_rating')))



    return render(request, 'Products/product_page.html', {
        'product': product,
        'ingredients':ingredients,
        'last_ingredient': ingredients[-1],
        'rating': product.rating,
        'liked': already_liked,
        'views':Browsing_History.objects.filter(product=product, interaction_type='view').count(),
    })

def SearchPage(request):
    if(request.method == 'POST'):
        searched_phrase = request.POST.get('search')
        # rest here
        products = Product.objects.all()
    elif(request.method == 'GET'):
        searched_phrase = request.GET.get('searched_phrase')
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
    else:
        products = Product.objects.all()
    products = Product.objects.all()


    return render(request, 'Products/search_page.html', {
        'products': products,
    })