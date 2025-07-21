from django.urls import path

from . import views

urlpatterns = [
    path('', views.QuizPage, name='quiz_page')
]