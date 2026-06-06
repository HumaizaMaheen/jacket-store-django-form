from django.db import models

# Create your models here.
from django.db import models

class Jacket(models.Model):

    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Unisex', 'Unisex'),
    ]

    MATERIAL_CHOICES = [
        ('Leather', 'Leather'),
        ('Synthetic', 'Synthetic'),
        ('Suede', 'Suede'),
    ]

    j_id = models.AutoField(primary_key=True)

    # 🧥 Basic Info
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)

    # 📦 Type
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    material = models.CharField(max_length=50, choices=MATERIAL_CHOICES)

    # 🎨 Details
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=20)

    # 💰 Pricing
    price = models.FloatField()
    stock = models.IntegerField()

    # 📝 Description
    description = models.TextField()

    # 🖼 Image
    image = models.ImageField(upload_to='jacket_images/', null=True, blank=True)

    def __str__(self):
        return self.name