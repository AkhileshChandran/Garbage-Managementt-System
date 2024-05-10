from django import forms
from my_work.models import UserGarbageBin,Complaint


class UserGarbageBinForm(forms.ModelForm):
    class Meta:
        model = UserGarbageBin
        fields = ['user', 'bin']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['user', 'issue']