from django.db import models
from django.contrib.postgres.fields import ArrayField
from Users.models import User
from Choices.models import EyeConcernChoices, SkinTypeChoices, SkinConcernsChoices, PreferenceChoices, QuestionChoices, AgeGroupChoices, LifeStyleChoices, QuestionTypeChoices, BudgetChoices
# Create your models here.

class QuizResults(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=50, choices=AgeGroupChoices.choices, default='20_30')
    skin_type = models.CharField(max_length=50, choices=SkinTypeChoices.choices)
    dryness = models.PositiveIntegerField()
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
    eye_concern = models.CharField(max_length=30, choices=EyeConcernChoices.choices)

    budget = models.CharField(max_length=20, choices=BudgetChoices.choices, default='medium')
    lifestyle = models.CharField(max_length=50, choices=LifeStyleChoices.choices, default='minimal')
    skin_image = models.ImageField(upload_to='skin_analysis/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz result for {self.user.username}"
    
class Question(models.Model):
    order = models.PositiveIntegerField(default=0)
    question = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255, 
        choices=QuestionTypeChoices.choices,
        default='single_choice')
    options = ArrayField(
        models.CharField(max_length=100),
        null=True,
        blank=True
    )
    def __str__(self):
        return f'{self.order}.{self.question}'
