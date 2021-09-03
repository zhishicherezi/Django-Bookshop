from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mailings import models

class MailingsAdmin(admin.ModelAdmin):
    list_display = ('mail_to', 'text', 'created')

admin.site.register(models.Mailing, MailingsAdmin)  # Use the customized options

