from django.shortcuts import render
from django.http import HttpResponse
from Quizzes.models import QuizResults
from django.contrib.auth.decorators import login_required
from Products.models import Product
from Routines.models import RoutinePlan, RoutineStep

def routine_home(request):
    return HttpResponse("Welcome to routines page!")

@login_required
def routine_generator_view(request):
    user = request.user
    try:
        quiz_data = QuizResults.objects.get(user=user)
    except QuizResults.DoesNotExist:
        return render(request, 'routines/routine.html', {'error': 'Please complete the quiz first.'})

    # استخراج داده‌ها از quiz_data
    age = quiz_data.data.get('age')  # e.g., "20 to 30"
    preferences = quiz_data.data.get('preferences', [])  # e.g., ["Vegan", "Fragrance-Free"]
    skin_type = quiz_data.data.get('skin_type')  # e.g., "Dry"
    concerns = quiz_data.data.get('concerns', [])  # max 3
    budget = quiz_data.data.get('budget')  # e.g., "50$ to 70$"
    eye_concern = quiz_data.data.get('eye_concern')  # e.g., "Dark Circles"
    dryness_level = quiz_data.data.get('dryness')  # int from 0 to 10

    # تعیین نوع روتین پیشنهادی
    routine_name = 'minimalist'
    if 'Dryness & Dehydration' in concerns or (skin_type == 'Dry' or dryness_level >= 7):
        routine_name = 'hydration'
    elif 'Dark Spots' in concerns or 'Hyperpigmentation' in concerns:
        routine_name = 'full'
    elif 'Acne-Prone' in concerns or skin_type == 'Oily':
        routine_name = 'minimalist'
    elif 'Early Signs of Aging' in concerns or 'Mature Skin' in concerns:
        routine_name = 'full'

    # تعیین مراحل روتین
    steps = []

    # مرحله پاک‌کننده
    if skin_type == 'Oily':
        steps.append({
            'order': 1,
            'description': 'Use a foaming cleanser to control oil',
            'product_name': 'Salicylic Acid Cleanser'
        })
    elif skin_type == 'Dry':
        steps.append({
            'order': 1,
            'description': 'Use a cream cleanser for hydration',
            'product_name': 'Cream Cleanser'
        })
    else:
        steps.append({
            'order': 1,
            'description': 'Use a gentle daily cleanser',
            'product_name': 'Gentle Cleanser'
        })

    # سرم متناسب با concern
    concern_serums = {
        'Dark Spots': 'Vitamin C Serum',
        'Hyperpigmentation': 'Vitamin C Serum',
        'Dryness & Dehydration': 'Hyaluronic Acid Serum',
        'Acne-Prone': 'Niacinamide Serum',
        'Early Signs of Aging': 'Retinol Serum',
        'Dullness': 'Niacinamide Serum',
    }
    serum_added = False
    for concern in concerns:
        if concern in concern_serums:
            steps.append({
                'order': 2,
                'description': f'Apply {concern_serums[concern]} to treat {concern.lower()}',
                'product_name': concern_serums[concern]
            })
            serum_added = True
            break

    if not serum_added:
        steps.append({
            'order': 2,
            'description': 'Apply a basic hydrating serum',
            'product_name': 'Hyaluronic Acid Serum'
        })

    # مرطوب‌کننده متناسب با سطح خشکی پوست
    moisturizer_name = 'Oil-Free Moisturizer' if skin_type == 'Oily' else (
        'Anti-Aging Moisturizer' if 'Aging' in ' '.join(concerns) else 'Glacier Cleanser')
    steps.append({
        'order': 3,
        'description': 'Use a moisturizer to seal hydration',
        'product_name': moisturizer_name
    })

    # ضدآفتاب اجباری برای انواع پوست
    steps.append({
        'order': 4,
        'description': 'Apply sunscreen with SPF 50 every morning',
        'product_name': 'SPF 50 Sunscreen'
    })

    # کرم دور چشم در صورت نیاز
    if eye_concern != 'No Eye Concern':
        steps.append({
            'order': 5,
            'description': f'Use an eye cream for {eye_concern.lower()}',
            'product_name': f'{eye_concern} Eye Cream'  # فرض بر این که در دیتابیس هست
        })

    # ایجاد یا جایگزینی روتین در دیتابیس
    plan, _ = RoutinePlan.objects.get_or_create(user=user, name=routine_name)
    plan.routine_steps.all().delete()

    for step in steps:
        try:
            product = Product.objects.get(name=step['product_name'])
        except Product.DoesNotExist:
            product = None

        RoutineStep.objects.create(
            routine_plan=plan,
            order=step['order'],
            description=step['description'],
            product=product
        )

    return render(request, 'routines/routine.html', {'routine_plan': plan})