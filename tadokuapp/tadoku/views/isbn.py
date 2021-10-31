from ..forms import IsbnForm
from django.views.generic.edit import FormView
from django.urls import reverse
from urllib.parse import urlencode
from ..models import Book


class IsbnView(FormView):
    template_name = 'tadoku/isbn.html'
    form_class = IsbnForm

    def get_success_url(self):
        # データベースをisbnで検索し、データベース上に本の情報があれば/bookに飛んで読んだ情報を登録
        # 無ければ/book/createに行って本を登録してから/bookで読んだ情報を登録する
        isbn = self.request.POST.get('isbn')
        print(self.request.POST)

        if isbn:
            if Book.objects.filter(isbn=isbn).exists():
                redirect_url = reverse('tadoku:book_regist')
            else:
                redirect_url = reverse('tadoku:book_create')
        parameters = urlencode(dict(isbn=isbn))
        url = f'{redirect_url}?{parameters}'

        return url
