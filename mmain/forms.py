from mmain.models import Cereal, Manufacturer
from django import forms

class UserSignUp(forms.Form):  
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class Search(forms.Form):
    search = forms.CharField(required=False)
    