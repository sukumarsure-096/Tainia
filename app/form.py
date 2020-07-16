from django import forms

from app.models import *

class user_form(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','password','email','first_name','last_name']
        widgets = {'password':forms.PasswordInput}



class profile_form(forms.ModelForm):
    class Meta():
        model = profile
        fields = ['pic']

