from django.contrib import admin
from .models import Book, ReadBook
# Register your models here.


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'words', 'series', 'yl')
    list_filter = ['yl']
    search_fields = ['isbn']


@admin.register(ReadBook)
class ReadBooksAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'read_at', 'created_at', 'rate')
    list_filter = ['reader', 'book']
    search_fields = ['reader']
