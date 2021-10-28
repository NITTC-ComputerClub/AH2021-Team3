from django.urls import path

from .views import IndexView, BooksListView

app_name = 'tadoku'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BooksListView.as_view(), name='books')
]
