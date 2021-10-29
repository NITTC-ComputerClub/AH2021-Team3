from django.db import models
from django.conf import settings


# Create your models here.


class Book(models.Model):
    title = models.CharField(null=False, max_length=255)
    words = models.IntegerField(null=False)
    series = models.CharField(null=True, blank=True, max_length=255)
    yl = models.FloatField(null=True, blank=True)
    isbn = models.CharField(null=False, unique=True, max_length=13)

    def __str__(self):
        return self.title + " : " + str(self.isbn)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class ReadBook(models.Model):
    RATE_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    comment = models.TextField(null=True, blank=True)
    rate = models.PositiveSmallIntegerField(
        null=True, blank=True, choices=RATE_CHOICES)
    read_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book.title + " : " + self.reader.username

    class Meta:
        verbose_name = "Read Book"
        verbose_name_plural = "Read Books"
