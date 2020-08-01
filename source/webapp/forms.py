from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=100, label='ФИО')
    email = forms.EmailField(label='Email')
    text = forms.CharField(max_length=500, label='Запись')
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')



