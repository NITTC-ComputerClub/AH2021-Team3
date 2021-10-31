from django.urls import path
from .views import IndexView, BooksListView, IsbnView, BookCreateView, ReadBookCreateView, BookDetailView

app_name = 'tadoku'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BooksListView.as_view(), name='books'),
    path('isbn/', IsbnView.as_view(), name='isbn'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/', ReadBookCreateView.as_view(), name='book_regist'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
