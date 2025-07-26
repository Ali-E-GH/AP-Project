from django.urls import path
from . import views
from .views import routine_generator_view

urlpatterns = [
    path('', views.routine_home, name='routine_home'),
    path('generate-routine/', routine_generator_view, name='routine_generator'),
]
