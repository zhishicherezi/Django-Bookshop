"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aeroport_codes import views as code_view
from books import views as book_view
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('cun/', code_view.get_code),
    path('', book_view.book_list),
    path('book/<int:book_id>', book_view.book),
    path('books/', book_view.book_list, name = "book-list"),
    path('book/', book_view.book, name="book"),
    path('author/<int:author_id>', book_view.author, name = 'author'),
    path('authors/', book_view.authors, name='authors'),
    path('series/<int:series_id>', book_view.series, name = 'series'),
    path('seriess/', book_view.seriess, name = 'seriess'),
    path('genre/<int:genre_id>', book_view.genre, name = 'genre'),
    path('genres/', book_view.genres, name = 'genres'),
    path('publisher/<int:publisher_id>', book_view.publisher, name = 'publisher'),
    path('publishers/', book_view.publishers, name = 'publishers'),
    path('spravochniki/', book_view.spr_list, name = 'spr')
]
