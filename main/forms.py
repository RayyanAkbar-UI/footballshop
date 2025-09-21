from django import forms
from django.forms import ModelForm
from main.models import Product
import re

class CurrencyField(forms.CharField):
    def clean(self, value):
        if value:
            # Remove currency symbol, dots, and commas
            cleaned_value = re.sub(r'[^\d]', '', value)
            try:
                return int(cleaned_value)
            except ValueError:
                raise forms.ValidationError("Please enter a valid price")
        return 0

class ProductForm(ModelForm):
    # Override price field to handle currency input
    price = CurrencyField(
        label="Price (Rp)",
        help_text="Enter price in Rupiah (e.g., Rp 500.000)"
    )
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'quantity', 'thumbnail']
    
    def clean_price(self):
        # Get the price from cleaned_data
        price = self.cleaned_data.get('price')
        if isinstance(price, str):
            # Remove currency symbol, dots, and other non-digit characters
            price = re.sub(r'[^\d]', '', price)
            try:
                return int(price)
            except ValueError:
                raise forms.ValidationError("Please enter a valid price")
        return price