from django.db import models

# Create your models here.

class SkinTypeChoices(models.TextChoices):

    OILY = "oily", "Oily"
    DRY = "dry", "Dry"
    COMBINATION = "combination", "Combination"
    SENSITIVE = "sensitive", "Sensitive"
    NORMAL = "normal", "Normal"

class ProductCategoryChoices(models.TextChoices):

    CLEANSER = "cleanser", "Cleanser"
    SERUM = "serum", "Serum"
    MOISTURIZER = "moisturizer", "Moisturizer"
    TONER = "toner", "Toner"
    SUNSCREEN = "sunscreen", "Sunscreen"

class PreferenceChoices(models.TextChoices):

    VEGAN = "vegan", "Vegan"
    FRAGRANCE_FREE = "fragrance-free", "Fragrance-Free"
    CRUELTY_FREE = "cruelty-free", "Cruelty-Free"
    ALCOHOL_FREE = "alcohol-free", "Alcohol-Free"
    NON_COMEDOGENIC = "non-comedogenic", "Non-Comedogenic"

class SkinConcernsChoices(models.TextChoices):

    ACNE = "acne", "Acne"
    REDNESS = "redness", "Redness"
    DARK_SPOTS = "dark-spots", "Dark Spots"
    AGING = "aging", "Aging"
    DULLNESS = "dullness", "Dullness"

class DeviseChoices(models.TextChoices):

    MOBILE = 'mobile', "Mobile"
    DESKTOP = 'desktop', 'Desktop'

class IngredientsChoices(models.TextChoices):

    NIACINAMIDE = 'niacinamide','Niacinamide'
    HYALURONIC_ACID = 'hyaluronic_acid','Hyaluronic Acid'
    SALICYLIC_ACID = 'salicylic_acid','Salicylic Acid'
    RETINOL = 'retinol','Retinol'
    VITAMIN_C = 'vitamin_c','Vitamin C'
    CERAMIDES = 'ceramides','Ceramides'
    GLYCOLIC_ACID = 'glycolic_acid','Glycolic Acid'
    ZINC_OXIDE = 'zinc_oxide','Zinc Oxide'
    TEA_TREE_OIL = 'tea_tree_oil','Tea Tree Oil'
    ALOE_VERA = 'aloe_vera','Aloe Vera'

class InteractionTypeChoices(models.TextChoices):

    VIEW = 'view', 'View'
    LIKE = 'like', 'Like'
    WISHLIST = 'wishlist', 'Wishlist'
    CART = 'cart', 'Cart'

class SeasonChoices(models.TextChoices):
    
    SPRING = 'spring', 'Spring'
    SUMMER = 'summer', 'Summer'
    AUTUMN = 'autumn', 'Autumn'
    WINTER = 'winter', 'Winter'

class QuestionChoices(models.TextChoices):

    MULTIPLECHOICE = 'multiple_choice', 'Multiple Choice'
    SLIDER = 'slider', 'Slider'
    