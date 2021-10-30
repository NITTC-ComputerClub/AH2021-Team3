from ..models import Book
from django.views.generic import DetailView


class BookDetailView(DetailView):
    template_name = 'tadoku/book_detail.html'
    model = Book
