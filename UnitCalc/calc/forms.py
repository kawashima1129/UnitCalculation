from django import forms
from django.forms import TextInput, Textarea
from .models import Unit
import re
from django.core.mail import send_mail
from django.conf import settings


class TimeTableForm(forms.Form):
    unit = forms.ModelChoiceField(
        label='',
        widget=forms.Select,
        queryset = Unit.objects.all(),
        error_messages={
            'required': "You didn't select a choice.",
            'invalid_choice': "invalid choice.",
        },
        initial = Unit.objects.get(subject_name='なし')
    )


    def calc(self,unit_list):
        unit_list = list(set(unit_list))#重複データを消去
        unit_dict = {'コア':0, '必修':0, '選択必修':0, '共通科目':0, '自由選択':0 }
        requirement_dict = {'コア':8, '必修':8, '選択必修':10, '共通科目':4, '自由選択':0}
        shortage_dict = {'コア':0, '必修':0, '選択必修':0, '共通科目':0, '自由選択':0 }
        recommended = {'コア':[], '必修':[], '選択必修':[], '共通科目':[]}

        completeunit = []
        for pk in unit_list:
            obj = Unit.objects.get(pk=pk)
            if(obj.subject_category == 'コア'):
               unit_dict['コア'] = unit_dict['コア'] + obj.number_unit
            elif(obj.subject_category == '必修'):
               unit_dict['必修'] = unit_dict['必修'] + obj.number_unit
            elif(obj.subject_category == '選択必修'):
                unit_dict['選択必修'] = unit_dict['選択必修'] + obj.number_unit
            elif(obj.subject_category == '共通科目'):
                unit_dict['共通科目'] = unit_dict['共通科目'] + obj.number_unit
            elif(obj.subject_category == '自由選択'):
                unit_dict['自由選択'] = unit_dict['自由選択'] + obj.number_unit
            
            completeunit.append(obj.pk)
        
        #履修してない単位の主キーを取得
        objs = Unit.objects.all()
        allunit = [obj.pk for obj in objs]
        lackunit = set(allunit) - set(completeunit)
        lackunit_list = list(lackunit)

    
        for pk in lackunit_list:
            obj = Unit.objects.get(pk=pk)
            if(obj.subject_category == 'コア'):
                recommended['コア'].append(obj.subject_name)
            elif(obj.subject_category == '必修'):
                recommended['必修'].append(obj.subject_name)
            elif(obj.subject_category == '選択必修'):
                recommended['選択必修'].append(obj.subject_name)
            elif(obj.subject_category == '共通科目'):
                recommended['共通科目'].append(obj.subject_name)

        sum = 0
        for k1, v1 in unit_dict.items():
            if requirement_dict[k1] - unit_dict[k1] <= 0:
                shortage_dict[k1] = 0
            else:
                shortage_dict[k1] = requirement_dict[k1] - unit_dict[k1]
            sum = sum + v1
        
        requiredunit = 34
        check = [k for k, v in shortage_dict.items() if v > 0] 
        result = True if sum >= requiredunit and not check else False
        
        
        result_dict = {'合否':result , '履修単位合計':sum, '不足単位合計':requiredunit-sum}
        summary ={'履修単位':unit_dict, '不足単位':shortage_dict, '総計':result_dict, 'おすすめ':recommended}
        return summary


    def shaping(self, preform):
        form_str = str(preform)
        matchOB = re.search("<select.+select>", form_str, flags=re.DOTALL)
        return matchOB.group()

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', required=True, widget=forms.TextInput(attrs={'class': 'form-control reset-border-radius',}))
    message = forms.CharField(label='お問い合わせ内容', 
                              widget=forms.Textarea(attrs={'cols':4, 'rows': 10, 'class': 'form-control reset-border-radius',}), 
                              required=True)

    # メール送信処理
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['name']
        message = self.cleaned_data['message']
        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to)
        
