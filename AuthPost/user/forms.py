from re import A
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    
    class Meta:
        password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
        password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        help_texts = {
            'username': None,
            'email': None,
            'password':None,
        }