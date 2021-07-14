from django import forms
from django.forms.models import ModelForm
from django.forms import Form
from django.forms.widgets import TextInput
from . import models
from accounts.models import CustomUser
from carts import models as a_models

class OrderCreateForm(Form):
    phone = forms.CharField(label='Телефон', required=True,)
    country = forms.CharField(label="Страна", required=True,)
    city = forms.CharField(label="Город", required=True,)
    index = forms.IntegerField(label="Индекс", required=True,)
    adress = forms.CharField(label="Адрес", required=True,)
    extra = forms.CharField(label="Доп информация", required=False)

   
class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = (
            'status',
        )