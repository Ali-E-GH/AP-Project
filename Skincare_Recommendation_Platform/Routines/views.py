from django.shortcuts import redirect, render
from django.http import HttpResponse
from Quizzes.models import QuizResults
from django.contrib.auth.decorators import login_required
from Products.models import Product
from Routines.models import RoutinePlan, RoutineStep

@login_required
def routine_generator_view(request):
    user = request.user
    try:
        quiz_data = QuizResults.objects.get(user=user)
    except QuizResults.DoesNotExist:
        return redirect('quiz_page')

    # استخراج داده‌ها از quiz_data
    age = quiz_data.age  # S "Under 20","20 to 30","30 to 40","Over 40"

    preferences = quiz_data.preferences  # M Vegan,Fragrance-Free,Cruelty-Free,Alcohol-Free,Non-Comedogenic

    skin_type = quiz_data.skin_type  # S Oily,Dry,Combination,Sensitive,Normal

    concerns = quiz_data.concerns  # M max 3 of Acne-Prone,Redness,"Dark Spots",Dullness,Hyperpigmentation,Oily/Blackheads,"Dryness & Dehydration","Early Signs of Aging","Mature Skin","Sensitive / Rosacea-prone"
    
    budget = quiz_data.budget  # S "Under 30$","30$ to 50$","50$ to 70$","Over 70$"
    
    eye_concern = quiz_data.eye_concern  # S "Drak Circles","Fine Lines & Wrinkles",Puffiness,"No Eye Concern"
    
    dryness_level = quiz_data.dryness  # int from 0 to 10

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
    step = 1
    # مرحله پاک‌کننده
    if skin_type == 'Oily':
        steps.append({
            'order': step,
            'description': 'Use a foaming cleanser to control oil',
            'product_name': 'Salicylic Acid Cleanser'
        })
        step+=1
    elif skin_type == 'Dry':
        if budget == 'Over 70$':
            steps.append({
                'order': step,
                'description': 'Use a cream cleanser for hydration',
                'product_name': 'Cream Cleanser'
            })
        else:
            steps.append({
                'order': step,
                'description': 'Use a cream cleanser for hydration',
                'product_name': 'Simple Gentle'
            })
        step+=1
    else:
        if age == 'Over 40':
            steps.append({
                'order': step,
                'description': 'Use a gentle daily cleanser',
                'product_name': 'Gentle Cleanser'
            })
        elif age in ["Under 20","20 to 30"]:
            steps.append({
                'order': step,
                'description': 'Use a gentle daily cleanser',
                'product_name': 'Good Intent Glow Grind Cleansing Balm'
            })
        else:
            if budget == 'Over 70$' and preferences in ['Vegan', 'Cruelty-Free']:
                steps.append({
                'order': step,
                'description': 'Use a good cleanser',
                'product_name': 'Glacier Foam'
            })

            else:
                steps.append({
                    'order': step,
                    'description': 'Use a gentle daily cleanser',
                    'product_name': 'Hydrating Cleanser'
                })
        step+=1

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
                'order': step,
                'description': f'Apply {concern_serums[concern]} to treat {concern.lower()}',
                'product_name': concern_serums[concern]
            })
            serum_added = True
            break

    if not serum_added:
        steps.append({
            'order': step,
            'description': 'Apply a basic hydrating serum',
            'product_name': 'Hyaluronic Acid Serum'
        })
    step+=1

    # مرطوب‌کننده متناسب با سطح خشکی پوست
    if budget in ["50$ to 70$","Over 70$"]:
        moisturizer_name = 'Oil-Free Moisturizer' if skin_type == 'Oily' else ('Anti-Aging Moisturizer' if 'Aging' in ' '.join(concerns) else 'Glacier Cleanser')
        steps.append({
            'order': step,
            'description': 'Use a moisturizer to seal hydration',
            'product_name': moisturizer_name
        })
        step+=1

    # ضدآفتاب اجباری برای انواع پوست
    steps.append({
        'order': step,
        'description': 'Apply sunscreen with SPF 50 every morning',
        'product_name': 'SPF 50 Sunscreen'
    })
    step+=1

    # کرم دور چشم در صورت نیاز
    if eye_concern != 'No Eye Concern':
        if budget in ["30$ to 50$","50$ to 70$"]:
            steps.append({
                'order': step,
                'description': f'Use an eye cream for {eye_concern.lower()}',
                'product_name': f'De-Bloat Soothing Eye Cream'
            })
        elif budget == "Over 70$":
            steps.append({
                'order': step,
                'description': f'Use an eye cream for {eye_concern.lower()}',
                'product_name': f'Black Rice Bakuchiol Eye Cream'
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

    return render(request, 'Routines/routine_page.html', {'routine_plan': plan})