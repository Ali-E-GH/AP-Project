from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.ProductPage, name='product_page'),
    path('search/', views.SearchPage, name='search_page'),
]