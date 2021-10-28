from django.contrib import admin
from .models import Books, ReadBooks
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    model = Books


class ReadBooksAdmin(admin.ModelAdmin):
    model = ReadBooks


admin.site.register(Books, BooksAdmin)
admin.site.register(ReadBooks, ReadBooksAdmin)
