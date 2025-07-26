from django.shortcuts import render, redirect
from .models import QuizResults, Question
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import QuizForm

def QuizPage(request):
    questions = Question.objects.all()
    
    if request.method == 'POST':
        try:
            # اعتبارسنجی داده‌ها
            if not request.POST.get('skin_type'):
                raise ValidationError("نوع پوست باید انتخاب شود")
                
            quiz_result, created = QuizResults.objects.update_or_create(
                user=request.user,
                defaults={
                    'skin_type': request.POST.get('skin_type'),
                    'concerns': request.POST.getlist('concerns'),
                    'preferences': request.POST.getlist('preferences'),
                    'budget_range_min': request.POST.get('budget_min'),
                    'budget_range_max': request.POST.get('budget_max'),
                }
            )
            return redirect('routine_generator')
            
        except ValidationError as e:
            return render(request, 'Quizzes/quiz_page.html', {
                'questions': questions,
                'error': str(e)
            })
    
    # برای GET و سایر موارد
    return render(request, 'Quizzes/quiz_page.html', {
        'questions': questions
    })

def quiz_view(request):
    # دریافت تمام سوالات به ترتیب مشخص شده
    questions = Question.objects.all().order_by('order')
    
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES, questions=questions)
        if form.is_valid():
            # ذخیره نتایج کوئیز
            quiz_result = QuizResults(
                user=request.user,
                skin_type=form.cleaned_data['skin_type'],
                concerns=form.cleaned_data.get('concerns', []),
                preferences=form.cleaned_data.get('preferences', []),
                budget=form.cleaned_data['budget'],
                lifestyle=form.cleaned_data['lifestyle'],
                skin_image=form.cleaned_data.get('skin_image')
            )
            quiz_result.save()
            
            messages.success(request, 'پاسخ‌های شما با موفقیت ثبت شد!')
            return redirect('routine_generator')
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quizzes/quiz.html', {
        'form': form,
        'progress': 25  # درصد پیشرفت (اختیاری) دوست داشتید حذفش کنید
    })