from django.urls import path

from . import views
urlpatterns = [
    path('like/', views.ToggleLike, name='add_like'),
    path('view/', views.AddView, name='add_view'),
]