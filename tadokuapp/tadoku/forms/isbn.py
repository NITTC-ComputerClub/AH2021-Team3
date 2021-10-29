from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator


class IsbnForm(forms.Form):
    isbn = forms.CharField(required=True, label="ISBN", validators=[
                           MaxLengthValidator(limit_value=13),
                           ])
