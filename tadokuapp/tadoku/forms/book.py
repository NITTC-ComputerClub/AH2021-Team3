from django import forms
from ..models import ReadBook


class ReadBookForm(forms.ModelForm):
    # ISBNデータの受け渡しのためにhidden属性のinputをつくる
    isbn = forms.CharField(max_length=13)

    class Meta:
        model = ReadBook
        fields = ('comment', 'rate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # isbnはhidden inputにしておく
        self.fields['isbn'].widget = forms.HiddenInput()
