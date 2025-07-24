from django.shortcuts import render
from django.http import HttpResponse

def routine_home(request):
    return HttpResponse("Welcome to routines page!")
