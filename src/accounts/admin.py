from django import forms
from django.contrib import admin
from . import models
from . import forms
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    add_form = forms.CreateAccountForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Для заказа',
            {
                'fields': (
                    'phone',
                    'country',
                    'city',
                    'index',
                    'adress1',
                    'adress2',
                    'extra'
                )
            }
        )
    )

admin.site.register(models.CustomUser, CustomUserAdmin)
# Register your models here.
