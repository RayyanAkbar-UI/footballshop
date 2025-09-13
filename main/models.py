import uuid
from django.db import models

class Shop(models.Model):
    
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='shop_images/', null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)