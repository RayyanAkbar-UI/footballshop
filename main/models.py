import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    JERSEY = 'Jersey'
    SHOES = 'Shoes'
    BALL = 'Ball'
    ACCESSORIES = 'Accessories'
    BAGS = 'Bags'

    CATEGORY_CHOICES = [
        (JERSEY, 'Jersey'),
        (SHOES, 'Shoes'),
        (BALL, 'Balls'),
        (ACCESSORIES, 'Accessories'),
        (BAGS, 'Bags'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=JERSEY
    )
    
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def formatted_price(self):
        try:
            price_value = int(self.price)
            price_str = str(price_value)
            result = ""
            for i in range(len(price_str)):
                if i > 0 and (len(price_str) - i) % 3 == 0:
                    result += "."
                result += price_str[i]
            return f"Rp {result}"
        except (ValueError, TypeError):
            import re
            digits_only = re.sub(r'[^\d]', '', str(self.price))
            if digits_only:
                return self.formatted_price(int(digits_only))
            return "Price unavailable"

class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

class Author(models.Model):

    bio = models.TextField()
    books = models.ManyToManyField(Book)
    user = models.ForeignKey(User, on_delete=models.CASCADE)