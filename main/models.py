import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="Uncategorized")
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def formatted_price(self):
        """Return the price formatted as currency string."""
        # Always ensure we're working with an integer
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
            # If conversion fails, try to extract just the digits
            import re
            digits_only = re.sub(r'[^\d]', '', str(self.price))
            if digits_only:
                return self.formatted_price(int(digits_only))
            return "Price unavailable"