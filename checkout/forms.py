from django import forms
from . import models

class CheckoutForm(forms.ModelForm):

    name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs=
            {
                'class': "form-control",
                "placeholder": "Your Name"
            }))

    first_address = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs=
            {
                'class': "form-control",
                "placeholder": "Your First Address"
            }))
    second_address = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs=
            {
                'class': "form-control",
                "placeholder": "Your Second Address"
            }))

    town = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs=
            {
                'class': "form-control",
                "placeholder": "Town or City"
            }))


    email_address = forms.EmailField(
        widget=forms.EmailInput(attrs=
            {
                'class': "form-control",
                "placeholder": "Email Address"
            }))

    phone_number = forms.IntegerField(
        widget=forms.NumberInput(attrs=
            {
                'class': "form-control",
                "placeholder": "Phone Number"
            }))

    class Meta:
        model = models.Checkout
        fields = ("name","first_address", "second_address","town","email_address","phone_number")