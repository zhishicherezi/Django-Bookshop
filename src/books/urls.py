from django.urls import path
from books import views as book_view
from books.views import BookListView, AuthorListView, BookDetailView, BookDeleteView, BookUpdateView, BookCreateView, Home

app_name = 'books'

urlpatterns = [
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
    path('spravochniki/', book_view.spr_list, name = 'spr'),
    #path('create-book/', book_view.book_create, name = 'book-create'),
    path('create-author/', book_view.book_create_author, name = 'create-author'),
    path('update-author/<int:author_id>', book_view.book_update_author, name = 'update-author'),
    path('delete-author/<int:author_id>', book_view.book_delete_author, name = 'delete-author'),
    path('create-series/', book_view.book_create_series, name = 'create-series'),
    path('update-series/<int:series_id>', book_view.book_update_series, name = 'update-series'),
    path('delete-series/<int:series_id>', book_view.book_delete_series, name = 'delete-series'),
    path('create-genre/', book_view.book_create_genre, name = 'create-genre'),
    path('update-genre/<int:genre_id>', book_view.book_update_genre, name = 'update-genre'),
    path('delete-genre/<int:genre_id>', book_view.book_delete_genre, name = 'delete-genre'),
    path('create-publisher/', book_view.book_create_publisher, name = 'create-publisher'),
    path('update-publisher/<int:publisher_id>', book_view.book_update_publisher, name = 'update-publisher'),
    path('delete-publisher/<int:publisher_id>', book_view.book_delete_publisher, name = 'delete-publisher'),
    path('', BookListView.as_view(), name = 'books-view'),
    path('authors-view/', AuthorListView.as_view(), name = 'authors-view'),
    path('book-view/<int:pk>/', BookDetailView.as_view(), name = 'book-view'),
    path('book-create-view/', BookCreateView.as_view(), name = 'book_create'),
    path('book-update/<int:pk>/', BookUpdateView.as_view(), name = 'book_update'),
    path('book-delete/<int:pk>/', BookDeleteView.as_view(), name = 'book_delete'),
]