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

    object_query = Browsing_History.objects.filter(user=request.user, product=product, interaction_type='like')
    already_liked = object_query.exists()

    if(request.POST.get('user_rating')):
        product.ratings.append(float(request.POST.get('user_rating')))



    return render(request, 'Products/product_page.html', {
        'product': product,
        'ingredients':ingredients,
        'last_ingredient': ingredients[-1],
        'rating': round(mean(product.ratings), 1),
        'liked': already_liked,
        'views':Browsing_History.objects.filter(product=product, interaction_type='view').count(),
    })