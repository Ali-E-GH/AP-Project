from django.urls import path
from . import views
from .views import routine_generator_view

urlpatterns = [
    path('', routine_generator_view, name='routine_generator'),
]
