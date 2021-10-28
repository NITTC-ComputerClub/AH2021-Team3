from django.views.generic import ListView
from ..models import ReadBook
from django.contrib.auth.mixins import LoginRequiredMixin


class BooksListView(LoginRequiredMixin, ListView):
    template_name = 'tadoku/books.html'
    model = ReadBook

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)  # Article.objects.all() と同じ結果

        reader = self.request.user
        queryset = queryset.filter(reader=reader)

        return queryset
