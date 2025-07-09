from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser, name='login_page'),
    path('signup/', views.SignupUser, name='signup_page'),
    path('logout/', views.LogoutUser, name='logout')
]