from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import models
from . import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView, CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.

class Home(TemplateView):
    template_name = 'books/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['low_price'] = models.Book.objects.filter(price__lte = 15)
        return context    
    
            
class BookListView(ListView):
    model = models.Book
    template_name = 'books/book_list.html'
    paginate_by = 8
    def get_queryset(self):
        qs = super().get_queryset()
        search =  self.request.GET.get('search')
        print(self.request.GET.get('search'))
        filter = (self.request.GET.get('filter'))
        order = (self.request.GET.get('order'))
        if filter == 'active':
            return qs.filter(active=True)
        elif filter == 'sold':
            return qs.filter(active=False)
        elif order == 'entry_date':
            return qs.order_by('created')[:4]
        elif order == 'book_name':
            return qs.order_by('book_name')
        elif order == 'rating':
            print(qs.order_by('-rating'))
            return qs.order_by('-rating')[:50] 
           
        elif search:
            return qs.filter(book_name__icontains=search)
        else:
            return qs
            
        


class BookDetailView(DetailView):
    model = models.Book

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.CreateBookForm
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.add_book'
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.change_book'
    model = models.Book
    form_class = forms.CreateBookForm
    success_url = reverse_lazy('books:books-view')

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy('books:books-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.delete_book'
    

# ОПИСАНИЕ СПРАВОЧНИКОВ АВТОР, ЖАНР, СЕРИЯ, ИЗДАТЕЛЬ

class AuthorListView(ListView):
    model = models.Author
    template_name = 'books/author_list.html'

class AuthorDetailView(DetailView):
    model = models.Author

class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = models.Author
    form_class = forms.CreateAuthorForm
    success_url = reverse_lazy('books:authors-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.add_author'
    
class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Author
    form_class = forms.CreateAuthorForm
    success_url = reverse_lazy('books:authors-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.change_author'

class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Author
    success_url = reverse_lazy('books:authors-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.delete_author'


class GenreListView(ListView):
    model = models.Genre
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get('order') == "alphabet":
         print(type(qs))
        return qs
class GenreDetailView(DetailView):
    model = models.Genre

class GenreCreateView(PermissionRequiredMixin, CreateView):
    model = models.Genre
    form_class = forms.CreateGenreForm
    success_url = reverse_lazy('books:genres-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.add_genre'
    
class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Genre
    form_class = forms.CreateGenreForm
    success_url = reverse_lazy('books:genres-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.change_genre'
class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Genre
    success_url = reverse_lazy('books:genres-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.delete_genre'

class SeriesListView(ListView):
    model = models.Series

class SeriesDetailView(DetailView):
    model = models.Series

class SeriesCreateView(PermissionRequiredMixin, CreateView):
    model = models.Series
    form_class = forms.CreateSeriesForm
    success_url = reverse_lazy('books:seriess-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.add_series'

class SeriesUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Series
    form_class = forms.CreateSeriesForm
    success_url = reverse_lazy('books:seriess-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.change_genre'

class SeriesDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Series
    success_url = reverse_lazy('books:seriess-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.delete_genre'

class PublisherListView(ListView):
    model = models.Publisher

class PublisherDetailView(DetailView):
    model = models.Publisher

class PublisherCreateView(PermissionRequiredMixin, CreateView):
    model = models.Publisher
    form_class = forms.CreatePublisherForm
    success_url = reverse_lazy('books:publishers-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.add_publisher'

class PublisherUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Publisher
    form_class = forms.CreatePublisherForm
    success_url = reverse_lazy('books:publishers-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.change_publisher'

class PublisherDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Publisher
    success_url = reverse_lazy('books:publishers-view')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = 'books.delete_publisher'

