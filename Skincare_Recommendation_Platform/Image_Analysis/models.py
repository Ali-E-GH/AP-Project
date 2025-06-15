from django.db import models
from django.contrib.postgres.fields import ArrayField

from Users.models import User
from Choices.models import SkinConcernsChoices
# Create your models here.

class ImageAnalysisResult(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_path = models.ImageField(upload_to='media/')
    detected_issues = ArrayField(
        models.CharField(max_length=30, choices=SkinConcernsChoices.choices),
        default=list,
        blank=True
    )
    confidence_scores = models.JSONField(default=list)
    analyzed_at = models.DateTimeField(auto_now_add=True)
