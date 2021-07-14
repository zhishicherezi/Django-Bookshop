from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'author', 'text', 'created'
    ]
admin.site.register(models.Comment, CommentAdmin)