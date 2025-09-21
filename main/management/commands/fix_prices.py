import re
from django.core.management.base import BaseCommand
from main.models import Product

class Command(BaseCommand):
    help = 'Fix formatted prices in the database'

    def handle(self, *args, **options):
        products = Product.objects.all()
        fixed_count = 0
        
        for product in products:
            # Check if price is a string or not an integer
            if not isinstance(product.price, int) or (isinstance(product.price, str) and product.price.startswith("Rp") or product.price.startswith("R.P")):
                # Extract digits only
                try:
                    # Get only digits from the price string
                    digits_only = re.sub(r'[^\d]', '', str(product.price))
                    product.price = int(digits_only)
                    product.save(update_fields=['price'])
                    fixed_count += 1
                    self.stdout.write(self.style.SUCCESS(f'Fixed price for product {product.id}: {product.name}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error fixing price for product {product.id}: {e}'))
        
        self.stdout.write(self.style.SUCCESS(f'Fixed {fixed_count} product prices'))