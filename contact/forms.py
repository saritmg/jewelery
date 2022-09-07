from django import forms
from . import models


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    email = forms.EmailField(
        max_length=50,
        widget=forms.EmailInput(attrs={'class': "form-control"}),
    )

    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    message = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={'class': "form-control"}),
    )

    class Meta:
        model = models.Contact
        fields = ("name", "email", "subject", "message")
        labels = {
            'name': 'Name',
        }