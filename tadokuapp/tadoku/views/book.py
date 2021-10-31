from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import redirect
from ..models import ReadBook, Book
from ..forms import ReadBookForm
import datetime


class BookCreateView(CreateView):
    # https://noumenon-th.net/programming/2019/11/18/django-createview/
    model = Book
    template_name = 'tadoku/book_create.html'
    fields = ('isbn', 'title', 'series', 'yl', 'words')

    def get(self, request, *args, **kwargs):
        # book/create/?isbn=1234567890123 の1234567890123の部分
        # GETパラメータからisbnを取り出し、インスタンス変数へ格納
        self.isbn = request.GET.get('isbn')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # POSTの時にself.isbnが無いと怒られるので追加 get_initial()がPOST時も呼ばれる
        # TODO:get_initial内で、self.isbnがあれば代入する処理に変えた方がいい
        self.isbn = request.POST.get('isbn')
        return super().post(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["isbn"] = self.isbn
        return initial

    def get_success_url(self) -> str:
        # 登録した本のisbnのパラメータを付けたurlを返す
        isbn = self.isbn
        redirect_url = reverse('tadoku:book_regist')
        parameters = urlencode(dict(isbn=isbn))
        url = f'{redirect_url}?{parameters}'
        print(url)
        return url


class ReadBookCreateView(LoginRequiredMixin, CreateView):
    # 前ページからのリダイレクトで、必ずデータベース上に存在する本のisbnがパラメータでついてくる
    # get_context_dataをオーバーライドし、ユーザー情報と本の情報を埋め込んでtemplate上で表示する
    # また、form_validをオーバーライドし、あらかじめ持っている本の情報とユーザー情報を追加して保存する
    # 参考:https://igreks.jp/dev/django-createview%E3%82%84updateview%E5%88%A9%E7%94%A8%E6%99%82%E3%80%81%E4%BB%BB%E6%84%8F%E3%81%AE%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E8%A3%8F%E5%81%B4%E3%81%A7%E4%BF%9D%E5%AD%98%E3%81%99%E3%82%8B/

    model = ReadBook
    template_name = 'tadoku/book.html'
    form_class = ReadBookForm
    success_url = 'tadoku:books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # contextにユーザー情報と本の情報を追加する
        isbn = self.request.GET.get('isbn')
        context['book'] = Book.objects.get(isbn=isbn)
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        # readerにはuserを入れる
        post.reader = self.request.user

        # bookには、hidden-inputで隠しておいた、urlパラメータからゲットしたisbnを基に本のオブジェクトを入れる
        isbn = form.cleaned_data.get('isbn')
        post.book = Book.objects.get(isbn=isbn)

        post.save()  # データベースへ保存
        return redirect('tadoku:books')

    def get_initial(self):
        initial = super().get_initial()
        # POST時にisbnが必要になるので、hidden inputにGETパラメータについているisbnを入れておく
        isbn = self.request.GET.get('isbn')
        initial['isbn'] = isbn
        # 今日の日付を初期値として入れておく
        initial['read_at'] = datetime.datetime.today()
        return initial
