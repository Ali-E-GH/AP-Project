from django.db import models
from django.contrib.postgres.fields import ArrayField

from Users.models import User
from Products.models import Product
# Create your models here.

class RoutinePlan(models.Model):
    PLAN_CHOICES = [
        ('full', 'Full Plan'),
        ('hydration', 'Hydration Plan'),
        ('minimalist', 'Minimalist Plan'),
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=255, choices=PLAN_CHOICES)
    steps = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_name_display()}"
    
class RoutineStep(models.Model):
    routine_plan = models.ForeignKey(RoutinePlan, on_delete=models.CASCADE, related_name="routine_steps")
    order = models.PositiveIntegerField()
    description = models.TextField()
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Step {self.order} for {self.routine_plan}"
    