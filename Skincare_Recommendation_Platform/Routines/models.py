from django.db import models
from django.contrib.postgres.fields import ArrayField

from Users.models import User
# Create your models here.

class RoutinePlan(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    steps = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
