from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import models
from . import forms
from django.urls import reverse
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

def book_create(request):
    if request.method == 'POST':
        form = forms.CreateBookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data.get('book_name')
           # obj = models.Book.objects.create(book_name=book_name)
            form.save()
            return HttpResponseRedirect('/')
        else:
            pass

    else:
        form = forms.CreateBookForm()

    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "book_create.html", context = ctx)

def book_create_author(request):
    if request.method == 'POST':
        form = forms.CreateAuthorForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            form.save()
            return HttpResponseRedirect(reverse('authors'))
        else:
            pass

    else:
        form = forms.CreateAuthorForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "author_create.html", context = ctx)

def book_update_author(request, author_id):
    if request.method == 'POST':
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(request.POST, instance=obj)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            form.save()
            return HttpResponseRedirect(reverse(viewname='authors'))
        else:
            pass

    else:
        obj = models.Author.objects.get(pk=author_id)
        form = forms.CreateAuthorForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "author_create.html", context = ctx)

def book_delete_author(request, author_id):
    if request.method == 'POST':
        obj = models.Author.objects.get(pk=author_id).delete()
        return HttpResponseRedirect(reverse('authors'))
    else:
        return render(request, template_name = "author_delete.html", context = {})

def book_create_series(request):
    if request.method == 'POST':
        form = forms.CreateSeriesForm(request.POST)
        if form.is_valid():
            series = form.cleaned_data.get('series')
            form.save()
            return HttpResponseRedirect(reverse('seriess'))
        else:
            pass

    else:
        form = forms.CreateSeriesForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "series_create.html", context = ctx)

def book_update_series(request, series_id):
    if request.method == 'POST':
        obj = models.Series.objects.get(pk=series_id)
        form = forms.CreateSeriesForm(request.POST, instance=obj)
        if form.is_valid():
            series = form.cleaned_data.get('series')
            form.save()
            return HttpResponseRedirect(reverse(viewname='seriess'))
        else:
            pass

    else:
        obj = models.Series.objects.get(pk=series_id)
        form = forms.CreateSeriesForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "series_create.html", context = ctx)

def book_delete_series(request, series_id):
    if request.method == 'POST':
        obj = models.Series.objects.get(pk=series_id).delete()
        return HttpResponseRedirect(reverse('seriess'))
    else:
        return render(request, template_name = "series_delete.html", context = {})

def book_create_genre(request):
    if request.method == 'POST':
        form = forms.CreateGenreForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data.get('genre')
            form.save()
            return HttpResponseRedirect(reverse('genres'))
        else:
            pass

    else:
        form = forms.CreateGenreForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "genre_create.html", context = ctx)

def book_update_genre(request, genre_id):
    if request.method == 'POST':
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(request.POST, instance=obj)
        if form.is_valid():
            genre = form.cleaned_data.get('genre')
            form.save()
            return HttpResponseRedirect(reverse(viewname='genres'))
        else:
            pass

    else:
        obj = models.Genre.objects.get(pk=genre_id)
        form = forms.CreateGenreForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "genre_create.html", context = ctx)

def book_delete_genre(request, genre_id):
    if request.method == 'POST':
        obj = models.Genre.objects.get(pk=genre_id).delete()
        return HttpResponseRedirect(reverse('genres'))
    else:
        return render(request, template_name = "genre_delete.html", context = {})

def book_create_publisher(request):
    if request.method == 'POST':
        form = forms.CreatePublisherForm(request.POST)
        if form.is_valid():
            publisher = form.cleaned_data.get('publisher')
            form.save()
            return HttpResponseRedirect(reverse(viewname=publishers))
        else:
            pass

    else:
        form = forms.CreatePublisherForm()
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "publisher_create.html", context = ctx)

def book_update_publisher(request, publisher_id):
    if request.method == 'POST':
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(request.POST, instance=obj)
        if form.is_valid():
            publisher = form.cleaned_data.get('publisher')
            form.save()
            return HttpResponseRedirect(reverse(viewname='publishers'))
        else:
            pass

    else:
        obj = models.Publisher.objects.get(pk=publisher_id)
        form = forms.CreatePublisherForm(instance=obj)
    ctx = {
        'form': form,
        'is_valid': form.is_valid()
    }
    return render(request, template_name = "publisher_create.html", context = ctx)

def book_delete_publisher(request, publisher_id):
    if request.method == 'POST':
        obj = models.Publisher.objects.get(pk=publisher_id).delete()
        return HttpResponseRedirect(reverse('publishers'))
    else:
        return render(request, template_name = "publisher_delete.html", context = {})

