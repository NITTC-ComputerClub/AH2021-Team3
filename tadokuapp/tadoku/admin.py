from django.contrib import admin
from .models import Book, ReadBook
from import_export import resources  
from import_export.admin import ImportExportModelAdmin  
from import_export.fields import Field 
# Register your models here.

class BookResource(resources.ModelResource):
    title = Field(attribute='title', column_name='Title')
    words = Field(attribute='words', column_name='Total Words')
    yl = Field(attribute='yl', column_name='YL')
    isbn = Field(attribute='isbn', column_name='ISBN')
    class Meta:
        model = Book
        skip_unchanged = True
        use_bulk = True

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    list_display = ('isbn', 'title', 'words', 'series', 'yl')
    list_filter = ['yl']
    search_fields = ['isbn']

@admin.register(ReadBook)
class ReadBooksAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book', 'read_at', 'created_at', 'rate')
    list_filter = ['reader', 'book']
    search_fields = ['reader']
