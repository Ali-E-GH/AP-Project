from django.db import models


from Users.models import User
from Products.models import Product
from Choices.models import InteractionTypeChoices

# Create your models here.
class Browsing_History(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    interaction_type = models.CharField(max_length=10, choices=InteractionTypeChoices.choices)

class Purchase_History(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

