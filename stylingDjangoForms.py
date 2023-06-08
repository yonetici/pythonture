from django import forms
from django.forms import TextInput, EmailInput

class UserInfoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
