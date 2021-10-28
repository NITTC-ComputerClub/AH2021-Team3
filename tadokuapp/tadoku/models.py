from django.db import models
from django.conf import settings


# Create your models here.


class Books(models.Model):
    title = models.CharField(null=False, max_length=100)
    words = models.IntegerField(null=False)
    series = models.CharField(null=True, blank=True, max_length=100)
    yl = models.SmallIntegerField(null=True, blank=True)
    isbn = models.CharField(null=False, unique=True, max_length=13)


class ReadBooks(models.Model):
    RATE_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]

    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=False)
    comment = models.CharField(null=True, blank=True, max_length=500)
    rate = models.SmallIntegerField(
        null=True, blank=True, choices=RATE_CHOICES)
    read_at = models.DateField(auto_now_add=True)
