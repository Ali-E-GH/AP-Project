from django.db import models
from django.contrib.postgres.fields import ArrayField
from Users.models import User
from Choices.models import SkinTypeChoices, SkinConcernsChoices, PreferenceChoices, QuestionChoices
# Create your models here.

class QuizResults(models.Model):
    AGE_GROUPS = [
        ('under_20', 'Under 20 years old'),
        ('20_30', '20 to 30 years'),
        ('30_40', '30 to 40 years'),
        ('over_40', 'Over 40 years old')
    ]
    
    LIFESTYLE_CHOICES = [
        ('minimal', 'Short time (maximum 3 steps)'),
        ('full', 'Desire for a complete routine (+5 steps)'),
        ('hydration', 'Focus on water supply'),
        ('anti_aging', 'Focus on anti-aging')
    ]
    
    BUDGET_CHOICES = [
        ('low', 'Under 5$'),
        ('medium', '5$ to 15$'),
        ('high', '15$ to 25$'),
        ('premium', 'Over 25$')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=50, choices=AGE_GROUPS, default='20_30')
    skin_type = models.CharField(max_length=50, choices=SkinTypeChoices.choices)
    concerns = ArrayField(
        models.CharField(max_length=30, choices=SkinConcernsChoices.choices),
        default=list,
        blank=True
    )
    preferences = ArrayField(
        models.CharField(max_length=30, choices=PreferenceChoices.choices),
        default=list,
        blank=True
    )
    budget_range_min = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    budget_range_max = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    lifestyle = models.CharField(max_length=50, choices=LIFESTYLE_CHOICES, default='minimal')
    skin_image = models.ImageField(upload_to='skin_analysis/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz result for {self.user.username}"
    
class Question(models.Model):
    QUESTION_TYPES = [
    ('text', 'Text Answer'),
    ('single_choice', 'Single Choice'),
    ('multiple_choice', 'Multiple Choice'),
    ('slider', 'Slider Scale'),
    ]
    # QUESTION_NAME = [
    #     ('skin_type', 'Skin'), 
    #     ('concerns', 'Concerns'),
    #     ('preferences', 'Preferences'),
    #     ('timestamp', 'Timestamp'),
    #     ('budget', 'Budget'),
    # ]
    # question_name = models.CharField(max_length=255, default='Your Question', choices=QUESTION_NAME)
    order = models.PositiveIntegerField(default=0)
    question = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255, 
        choices=QUESTION_TYPES,
        default='single_choice')
    options = ArrayField(
        models.CharField(max_length=100),
        null=True,
        blank=True
    )
    # created_date = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     ordering = ['-created_date']
        
    def __str__(self):
        return self.question
