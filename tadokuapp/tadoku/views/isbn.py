from ..forms import IsbnForm
from django.views.generic.edit import FormView


class IsbnView(FormView):
    template_name = 'tadoku/isbn.html'
    form_class = IsbnForm  # forms.pyで作ったFormクラスをここで使う
    # success_url = 'result' # formに入力された値が正しければこのURLに飛ぶ
