from django.shortcuts import render , HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

import json

from Products.models import Product
from History.models import Browsing_History, Purchase_History

from .models import UserProfile, Cart, CartItem

def SignupUser(request):
    is_empty = False
    not_match = False
    username_exists = False

    if(request.method == 'POST'):
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        repeat_password = request.POST.get('password_confirmation')  

        if(password != repeat_password):
            not_match = True

        if(not username or not password):
            is_empty = True

        if(User.objects.filter(username=username).exists()):
            username_exists = True

        if not(is_empty or not_match or username_exists):
        
            user = User.objects.create_user(username=username, password=password)
            UserProfile.objects.create(user=user)
            Cart.objects.create(user=user)

            user.save()
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'Users/Signup.html', {
                'is_empty': is_empty,
                'not_match': not_match,
                'username_exists': username_exists
                })
    else:

        return render(request, 'Users/Signup.html', {})


def LoginUser(request):
    is_empty = False
    is_wrong = False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')  # Check POST first

        if username == '' or password == '':
            is_empty = True
            return render(request, 'Users/Login.html', {'is_empty': is_empty, 'is_wrong': is_wrong, 'next': next_url})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("home_page")
        else:
            is_wrong = True
            return render(request, 'Users/Login.html', {'is_empty': is_empty, 'is_wrong': is_wrong, 'next': next_url})

    else:
        next_url = request.GET.get('next')  # On GET, read next from query string
        return render(request, 'Users/Login.html', {'next': next_url})


def LogoutUser(request):
    logout(request)
    return redirect("home_page")


def AddToCart(request):
    if not(request.user.is_authenticated):
        return JsonResponse({'redirect_url': '/user/login/'}, status=401)
    if not(request.user.cart):
        Cart.objects.create(user=request.user)
        
    data = json.loads(request.body)

    product_id = data.get('product_id')
    product = get_object_or_404(Product, id=product_id)

    quantity = int(data.get('quantity'))

    if(CartItem.objects.filter(cart=request.user.cart, product=product).exists()):
        cart_item = get_object_or_404(CartItem, cart=request.user.cart, product=product)
        cart_item.quantity += quantity
        cart_item.save(update_fields=['quantity'])
    else:
        cart_item = CartItem.objects.create(cart=request.user.cart, product=product, quantity=quantity)
        Browsing_History.objects.create(user=request.user, product=product, interaction_type='cart')
        

    return JsonResponse({'success': True})

@login_required
def CartPage(request):
    if(request.user.cart):
        cart = request.user.cart
        cart_items = cart.items.all()
    else:
        Cart.objects.create(user=request.user)

    return render(request, 'Users/cart_page.html', {'items': cart_items, 'cart':cart})

@login_required
def AddAndRemove(request):
    
    data = json.loads(request.body)
    item_id = data.get('id')
    action = data.get('action')
    cart = request.user.cart
    cart_item = get_object_or_404(CartItem, id=item_id)

    if(action == 'add'):
        cart_item.quantity += 1
        cart_item.save(update_fields=['quantity'])
    if(action == 'remove'):
        if(cart_item.quantity == 1):
            cart_item.delete()
            return JsonResponse({'status': 'deleted'})
        else:
            cart_item.quantity -= 1
            cart_item.save(update_fields=['quantity'])

    return JsonResponse({
        'status':'success',
        'total_cost': cart_item.total_cost,
        'total_cart_cost': cart.total_cost,
        'total_cart_quantity':cart.total_items
        })

@login_required
def CompletePurchase(request):
    cart = request.user.cart
    cart_items = cart.items.all()
    for item in cart_items:
        Purchase_History.objects.create(user=request.user, product=item.product, quantity=item.quantity)
        item.delete()
    return JsonResponse({'status': 'success'})