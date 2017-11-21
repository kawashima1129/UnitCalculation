from django import forms
from .models import Unit


class TimeTableForm(forms.Form):
    unit = forms.ModelChoiceField(
        label='',
        widget=forms.Select,
        queryset = Unit.objects.all(),
        error_messages={
            'required': "You didn't select a choice.",
            'invalid_choice': "invalid choice.",
        },
        initial=Unit.objects.get(subject_name='なし')
    )

    def calc(self):
        pass
        #assert(self.is_valid())

class MyForm(forms.Form):
	text = forms.CharField(max_length=100, required=False, label='テキスト')
