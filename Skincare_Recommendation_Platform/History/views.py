from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from Products.models import Product
from .models import Browsing_History
import json
# Create your views here.

def AddView(request):

    if(request.method == 'POST'):

        data = json.loads(request.body)
        product_id = data.get('product_id')

        product = get_object_or_404(Product, id=product_id)

        Browsing_History.objects.create(user=request.user, product=product, interaction_type='view')
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def ToggleLike(request):

    if(request.method == 'POST'):
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        object_query = Browsing_History.objects.filter(user=request.user, product=product, interaction_type='like')

        already_liked = object_query.exists()

        if(already_liked):
            object_query.delete()
        else:
            Browsing_History.objects.create(user=request.user, product=product, interaction_type='like')

        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)