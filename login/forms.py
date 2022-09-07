from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(min_length= 5, widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username","first_name", "last_name","email", "password")
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'password': 'Password'
        }

