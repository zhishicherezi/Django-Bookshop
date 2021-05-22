from django.contrib import admin
from django.contrib.admin.decorators import display
from . import models
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'book_name', 'created', 'entry_date'
    ]
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author']
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['series']
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre']
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['publisher']
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Author, AuthorAdmin)
