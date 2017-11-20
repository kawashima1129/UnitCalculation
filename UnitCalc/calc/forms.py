from django import forms
from .models import Unit

CHOICE = {
    ('0','キュート'),
    ('1','クール'),
    ('2','パッション'),
}

class TimeTableForm(forms.Form):
    unit = forms.ModelChoiceField(
        label='教科',
        widget=forms.Select,
        #widget=forms.RadioSelect,
        queryset = Unit.objects.all()
    )
