from . import models
from django import forms

class CreateCartForm(forms.ModelForm):
    class Meta:
        model = models.BooksInCart
        fields = (
            'quantity',
            'book',
            'unit_price',
        
        ) 
