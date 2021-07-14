from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'phone', 'created', 'updated', 'customer'
    ]

class StatusAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'status'
    ]

admin.site.register(models.OrderStatus, StatusAdmin)
admin.site.register(models.Order, OrderAdmin)

