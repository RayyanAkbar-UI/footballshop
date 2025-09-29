import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    # 1. Definisikan konstanta untuk pilihan kategori
    JERSEY = 'Jersey'
    SHOES = 'Shoes'
    BALL = 'Ball'
    ACCESSORIES = 'Accessories'
    BAGS = 'Bags'

    # 2. Buat daftar pilihan (choices) yang akan digunakan oleh Django
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
    
    # 3. Hubungkan field 'category' dengan daftar pilihan yang baru dibuat
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=JERSEY
    )
    
    # TAMBAHKAN KEMBALI FIELD GAMBAR
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def formatted_price(self):
        """Return the price formatted as currency string."""
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