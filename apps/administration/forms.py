from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'poste',
            'departements',
            'directions',
            'filiales',
            'password1', 
            'password2', 
            ]

class EditUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name', 
            'last_name', 
            'email',
            'poste',
            'departements',
            'directions',
            'filiales',
            ]