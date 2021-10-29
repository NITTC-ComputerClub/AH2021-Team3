from django.urls import path

from .views import IndexView, BooksListView, IsbnView

app_name = 'tadoku'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BooksListView.as_view(), name='books'),
    path('isbn/', IsbnView.as_view(), name='isbn'),
]
