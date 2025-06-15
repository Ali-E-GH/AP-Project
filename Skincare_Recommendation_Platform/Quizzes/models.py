from django.db import models
from django.contrib.postgres.fields import ArrayField

from Users.models import User
from Choices.models import SkinTypeChoices, SkinConcernsChoices, PreferenceChoices
# Create your models here.

class QuizResults(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skin_type = models.CharField(max_length=30, choices=SkinTypeChoices.choices)
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
    timestamp = models.DateTimeField(auto_now_add=True)
    budget_range_min = models.DecimalField(max_digits=8, decimal_places=2)
    budget_range_max = models.DecimalField(max_digits=8, decimal_places=2)
    
