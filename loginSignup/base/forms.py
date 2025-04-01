from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    middle_name = forms.CharField(max_length=30, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser 
        fields = ['username', 'first_name', 'last_name', 'middle_name', 'phone_number', 'email', 'password1', 'password2']