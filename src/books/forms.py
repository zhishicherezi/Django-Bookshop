from django import forms
from django.http import request
from . import models


# форма для новой книги
class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            'book_photo',
            'book_name',
            'book_price',
            'author',
            'series',
            'genre',
            'published',
            'pages',
            'pereplet',
            'ISBN',
            'weight',
            'age_protect',
            'publisher',
            'active',
            'rating'
        ) 

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'author',
        ) 
    def clean_form(self):
        value = self.cleaned_data.get('author')
        if value == '5uk4':
            raise ValidationError('Не обзывайся')
class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = (
            'series',
        ) 
class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'genre',
        ) 
class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = (
            'publisher',
        ) 