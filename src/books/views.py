from django.shortcuts import render
from . import models
# Create your views here.
def book(request, book_id):
    book = models.Book.objects.get(pk=book_id)
    ctx = {
        'book': book
    }
    return render(request, template_name = "book_detail.html", context = ctx)

def book_list(request):
    book_list = models.Book.objects.all()
    ctx = {
        'book_list': book_list
    }
    return render(request, template_name = "book_list.html", context = ctx)

def author(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    ctx = {
        'author': author
    }
    return render(request, template_name = 'author.html', context = ctx)

def authors(request):
    authors = models.Author.objects.all()
    ctx = {
        'authors': authors
    }
    return render(request, template_name = 'authors.html', context = ctx)

def series(request, series_id):
    series = models.Series.objects.get(pk=series_id)
    ctx = {
        'series': series
    }
    return render(request, template_name = 'series.html', context = ctx)

def seriess(request):
    seriess = models.Series.objects.all()
    ctx = {
        'seriess': seriess
    }
    return render(request, template_name = 'seriess.html', context = ctx)

def genre(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    ctx = {
        'genre': genre
    }
    return render(request, template_name = 'genre.html', context = ctx)

def genres(request):
    genres = models.Genre.objects.all()
    ctx = {
        'genres': genres
    }
    return render(request, template_name = 'genres.html', context = ctx)
    
def publisher(request, publisher_id):
    publisher = models.Publisher.objects.get(pk=publisher_id)
    ctx = {
        'publisher': publisher
    }
    return render(request, template_name = 'publisher.html', context = ctx)   

def publishers(request):
    publishers = models.Publisher.objects.all()
    ctx = {
        'publishers': publishers
    }
    return render(request, template_name = 'publishers.html', context = ctx)


def spr_list(request):
    author = models.Author.objects.all()
    series = models.Series.objects.all()
    genre = models.Genre.objects.all()
    publisher = models.Publisher.objects.all()
    ctx = {
        'author': author,
        'series': series,
        'genre': genre,
        'publisher': publisher
    }
    return render(request, template_name = "spr_list.html", context = ctx)

