from django.db import models

from Users.models import User
from Choices.models import DeviseChoices, SeasonChoices
# Create your models here.

class ContextualData(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    device_type = models.CharField(max_length=25, choices=DeviseChoices.choices)
    season = models.CharField(max_length=15, choices=SeasonChoices.choices)
