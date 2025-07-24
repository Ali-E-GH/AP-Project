from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from Choices.models import DeviseChoices, SkinTypeChoices, SkinConcernsChoices, PreferenceChoices
from Products.models import Product

# Create your models here.
class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart', null=True)

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all()) # type: ignore
    
    @property
    def total_cost(self):
        return sum((item.quantity * item.product.price) for item in self.items.all()) # type: ignore
    
class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return  self.quantity * self.product.price
    class Meta:
        unique_together = ('cart', 'product')
