from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser, name='login_page'),
    path('signup/', views.SignupUser, name='signup_page'),
    path('logout/', views.LogoutUser, name='logout'),
    path('add_to_cart/', views.AddToCart, name='add_to_cart'),
    path('cart/', views.CartPage, name='cart_page'),
    path('item_quantity/', views.AddAndRemove, name='add_and_remove'),
    path('purchase/', views.CompletePurchase, name='purchase'),
]