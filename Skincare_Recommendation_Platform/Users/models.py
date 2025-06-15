from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from Choices.models import DeviseChoices, SkinTypeChoices, SkinConcernsChoices, PreferenceChoices

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_device = models.CharField(max_length=25, choices=DeviseChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    skin_type = models.CharField(max_length= 30, choices=SkinTypeChoices.choices)
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
    



    @property
    def name(self):
        return f"{self.user.first_name} {self.user.last_name}"