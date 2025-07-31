from django.shortcuts import render
from django.http import HttpResponse
from Quizzes.models import QuizResults

def routine_home(request):
    return HttpResponse("Welcome to routines page!")

def routine_generator_view(request):
    quiz_data = QuizResults.objects.get(user=request.user)
    # منطق ساخت روتین براساس quiz_data
    routine_plans = {
        'Full Plan': [
            {'step': 'Cleanser', 'product': 'Product A'},
            {'step': 'Moisturizer', 'product': 'Product B'}
        ]
    }
    return render(request, 'routines/routine.html', {'routine': routine_plans})