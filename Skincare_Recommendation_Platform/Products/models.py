from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms

from Choices.models import IngredientsChoices, SkinTypeChoices, SkinConcernsChoices, PreferenceChoices, ProductCategoryChoices

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length= 255)
    brand = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=30, choices=ProductCategoryChoices.choices)
    description = models.CharField(max_length=1000, blank=True, null=True)
    ratings = ArrayField(
        models.FloatField(),
        default=list,
        blank=True,
    )
    compatible_skin_types = ArrayField(
        models.CharField(max_length=30, choices=SkinTypeChoices.choices),
        default=list,
        blank=True
    )
    concerns_targeted = ArrayField(
        models.CharField(max_length=30, choices=SkinConcernsChoices.choices),
        default=list,
        blank=True          
    )
    ingredients = ArrayField(
        models.CharField(max_length=30, choices=IngredientsChoices.choices),
        default=list,
        blank=True
    )
    image_url = models.CharField(max_length=255, blank=True, null=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True,
        null=True
    )

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         widgets = {
#             'ingredients': 
#         }