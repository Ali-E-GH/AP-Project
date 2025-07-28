from django.shortcuts import render, redirect
from .models import QuizResults, Question
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import QuizForm

from .models import Question
# Create your views here.
def QuizPage(request):
    questions = Question.objects.all()
    answers = {}
    if(request.method == 'POST'):
        for question in questions:
            key = f'question_{question.id}' # type: ignore
            if(question.type == 'multiple_choice'):
                answer = request.POST.getlist(key)
            elif(question.type == 'single_choice'):
                answer = request.POST.getlist(key)
            else:
                answer = request.POST.get(key)
            answers[question.id] = answer # type: ignore

    return render(request, 'Quizzes/quiz_page.html', {'questions': questions})