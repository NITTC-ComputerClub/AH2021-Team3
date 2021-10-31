from django import forms
from ..models import ReadBook


class ReadBookForm(forms.ModelForm):
    # ISBNデータの受け渡しのためにhidden属性のinputをつくる
    isbn = forms.CharField(max_length=13)
    # read_at = forms.DateField(initial=datetime.date.today, widget=AdminDateWidget())

    class Meta:
        model = ReadBook
        fields = ('read_at', 'comment', 'rate')
        widget = {
            'read_at': forms.DateInput(attrs={'class': 'datepicker'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # isbnはhidden inputにしておく
        self.fields['isbn'].widget = forms.HiddenInput()
