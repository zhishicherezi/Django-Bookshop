from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import BookSerializer
from books.models import Book

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """API ENDPOINT"""
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('-ISBN')
#     queryset = User.objects.all().order_by('-date_joined')


