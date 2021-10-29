from django.contrib import admin
from .models import Book, ReadBook
# Register your models here.


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    pass


@admin.register(ReadBook)
class ReadBooksAdmin(admin.ModelAdmin):
    pass
