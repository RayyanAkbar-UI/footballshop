from django import forms
from django.forms import ModelForm
from main.models import Product
import re

class CurrencyField(forms.CharField):
    def clean(self, value):
        if value:
            cleaned_value = re.sub(r'[^\d]', '', value)
            try:
                return int(cleaned_value)
            except ValueError:
                raise forms.ValidationError("Please enter a valid price")
        return 0

class ProductForm(ModelForm):
    price = CurrencyField(
        label="Price (Rp)",
        help_text="Enter price in Rupiah (e.g., Rp 500.000)"
    )
    
    class Meta:
        model = Product
        # Tambahkan 'quantity' ke dalam daftar fields
        fields = ['name', 'price', 'description', 'quantity', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-900/50 text-white border border-white/20 rounded-md p-2 mt-1 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-900/50 text-white border border-white/20 rounded-md p-2 mt-1 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            # Tambahkan widget untuk quantity
            'quantity': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-900/50 text-white border border-white/20 rounded-md p-2 mt-1 focus:ring-indigo-500 focus:border-indigo-500',
                'min': '0' # Opsional: mencegah nilai negatif
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-gray-900/50 text-white border border-white/20 rounded-md p-2 mt-1 h-24 focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'category': forms.HiddenInput(),
            # Tambahkan widget untuk input file gambar
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-purple-900/30 file:text-purple-300 hover:file:bg-purple-900/40'
            }),
        }
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if isinstance(price, str):
            price = re.sub(r'[^\d]', '', price)
            try:
                return int(price)
            except ValueError:
                raise forms.ValidationError("Please enter a valid price")
        return price