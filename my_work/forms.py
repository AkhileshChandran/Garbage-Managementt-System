from django import forms
from my_work.models import User, GarbageBin, UserGarbageBin, CollectionRequest, CollectionStatus, Complaint
from django.contrib.auth.forms import AuthenticationForm
from my_work.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Phone', max_length=13)

    class Meta:
        model = User
        fields = ['username', 'password']

  


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name','password', 'phone', 'email', 'address', 'user_type']

class GarbageBinForm(forms.ModelForm):
    class Meta:
        model = GarbageBin
        fields = ['name', 'price', 'assigned']



class CollectionRequestForm(forms.ModelForm):
    class Meta:
        model = CollectionRequest
        fields = ['garbage', 'status', 'request_status', 'driver']

class CollectionStatusForm(forms.ModelForm):
    class Meta:
        model = CollectionStatus
        fields = ['collectonrequest', 'request_status']


