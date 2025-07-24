from django.urls import path
from . import views

urlpatterns = [
    path('', views.routine_home, name='routine_home'),
]
