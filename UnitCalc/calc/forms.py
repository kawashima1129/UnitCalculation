from django import forms
from .models import Unit


class TimeTableForm(forms.Form):
    unit = forms.ModelChoiceField(
        label='',
        widget=forms.Select,
        queryset = Unit.objects.all()

    )

    def calc(self):
        pass

class MyForm(forms.Form):
	text = forms.CharField(max_length=100, required=False, label='テキスト')
