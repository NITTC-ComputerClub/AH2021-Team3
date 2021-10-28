from django.contrib import admin
from .models import Book, ReadBook
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    model = Book


class ReadBooksAdmin(admin.ModelAdmin):
    model = ReadBook


admin.site.register(Book, BooksAdmin)
admin.site.register(ReadBook, ReadBooksAdmin)
