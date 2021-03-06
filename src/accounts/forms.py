
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class CreateAccountForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'phone',
            'country',
            'city',
            'index',
            'adress1',
            'adress2'
        ) 

class UserAccountForm(ModelForm):
    class Meta:
        model = models.CustomUser
        fields = (
            '__all__'
        )

class UpdateProfiletForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone',
            'country',
            'city',
            'index',
            'adress1',
        ) 