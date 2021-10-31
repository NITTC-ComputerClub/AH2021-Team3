from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator


class IsbnForm(forms.Form):
    # TODO:フィールドの設定をもう少しつめる
    isbn = forms.CharField(required=True, label="ISBN", validators=[
                           MaxLengthValidator(limit_value=13),
                           ],
                           widget=forms.TextInput(attrs={
                               'id': 'isbn',
                               'placeholder': '数字のみ入力可能です。',
                               'pattern': '^[0-9]+$'}))
