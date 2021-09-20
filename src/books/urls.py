from django.urls import path
from books.views import BookListView, BookDetailView, BookDeleteView, BookUpdateView, BookCreateView
from books.views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
from books.views import SeriesCreateView, SeriesDeleteView, SeriesDetailView, SeriesListView, SeriesUpdateView
from books.views import GenreCreateView, GenreDeleteView, GenreDetailView, GenreListView, GenreUpdateView
from books.views import PublisherCreateView, PublisherDeleteView, PublisherDetailView, PublisherListView, PublisherUpdateView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name = 'books-view'),
    path('book-view/<int:pk>/', BookDetailView.as_view(), name = 'book-view'),
    path('book-create-view/', BookCreateView.as_view(), name = 'book_create'),
    path('book-update/<int:pk>/', BookUpdateView.as_view(), name = 'book_update'),
    path('book-delete/<int:pk>/', BookDeleteView.as_view(), name = 'book_delete'),
    path('authors/', AuthorListView.as_view(), name = 'authors-view'),                    #Автор
    path('author-view/<int:pk>/', AuthorDetailView.as_view(), name = 'author-view'),      #Автор
    path('author-create-view/', AuthorCreateView.as_view(), name = 'author_create'),      #Автор
    path('author-update/<int:pk>/', AuthorUpdateView.as_view(), name = 'author_update'),  #Автор
    path('author-delete/<int:pk>/', AuthorDeleteView.as_view(), name = 'author_delete'),  #Автор
    path('seriess/', SeriesListView.as_view(), name = 'seriess-view'),                    #Серия           
    path('series-view/<int:pk>/', SeriesDetailView.as_view(), name = 'series-view'),      #Серия
    path('series-create-view/', SeriesCreateView.as_view(), name = 'series_create'),      #Серия
    path('series-update/<int:pk>/', SeriesUpdateView.as_view(), name = 'series_update'),  #Серия
    path('series-delete/<int:pk>/', SeriesDeleteView.as_view(), name = 'series_delete'),  #Серия
    path('genres/', GenreListView.as_view(), name = 'genres-view'),                    #Жанр
    path('genre-view/<int:pk>/', GenreDetailView.as_view(), name = 'genre-view'),      #Жанр
    path('genre-create-view/', GenreCreateView.as_view(), name = 'genre_create'),      #Жанр
    path('genre-update/<int:pk>/', GenreUpdateView.as_view(), name = 'genre_update'),  #Жанр   
    path('genre-delete/<int:pk>/', GenreDeleteView.as_view(), name = 'genre_delete'),  #Жанр   
    path('publishers/', PublisherListView.as_view(), name = 'publishers-view'),                    #Издательство
    path('publisher-view/<int:pk>/', PublisherDetailView.as_view(), name = 'publisher-view'),      #Издательство
    path('publisher-create-view/', PublisherCreateView.as_view(), name = 'publisher_create'),      #Издательство
    path('publisher-update/<int:pk>/', PublisherUpdateView.as_view(), name = 'publisher_update'),  #Издательство   
    path('publisher-delete/<int:pk>/', PublisherDeleteView.as_view(), name = 'publisher_delete'),  #Издательство   
]
