from django import forms
from .models import Unit
import re


class TimeTableForm(forms.Form):
    unit = forms.ModelChoiceField(
        label='',
        widget=forms.Select,
        queryset = Unit.objects.all(),
        error_messages={
            'required': "You didn't select a choice.",
            'invalid_choice': "invalid choice.",
        },
        initial = Unit.objects.get(subject_name='なし'),
                                  #renderer.inner_html = '{ unit_value }'
    )
    """
    def __init__(self, *args, **kwargs):
        self.fields['unit'].widget.renderer.inner_html = '{ unit_value }'
        print('aa')
"""

    def calc(self,unit_list):
        unit_list = list(set(unit_list))#重複データを消去
        unit_dict = {'コア':0, '必修':0, '選択必修':0, '共通科目':0, '自由選択':0 }
        requirement_dict = {'コア':8, '必修':8, '選択必修':10, '共通科目':4, '自由選択':0}
        shortage_dict = {'コア':0, '必修':0, '選択必修':0, '共通科目':0, '自由選択':0 }
        
        for pk in unit_list:
           obj = Unit.objects.get(pk=pk)
           if(obj.subject_category == '必修'):
               unit_dict['コア'] = unit_dict['コア'] + obj.number_unit
           elif(obj.subject_category == '必修'):
               unit_dict['必修'] = unit_dict['必修'] + obj.number_unit
           elif(obj.subject_category == '選択必修'):
                unit_dict['選択必修'] = unit_dict['選択必修'] + obj.number_unit
           elif(obj.subject_category == '共通科目'):
                unit_dict['共通科目'] = unit_dict['共通科目'] + obj.number_unit


        sum = 0
        for k1, v1 in unit_dict.items():
            if requirement_dict[k1] - unit_dict[k1] <= 0:
                shortage_dict[k1] = 0
            else:
                shortage_dict[k1] = requirement_dict[k1] - unit_dict[k1]
            sum = sum + v1
       
        result_dict = {'必要単位合計':34, '履修単位':sum}

        summary ={'履修単位':unit_dict, '不足単位':shortage_dict, '総計':result_dict}
        return summary

    def shaping(self, preform):
        form_str = str(preform)
        matchOB = re.search("<select.+select>", form_str, flags=re.DOTALL)
        return matchOB.group()

        
        
