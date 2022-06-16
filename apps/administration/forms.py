from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'sexe',
            'email',
            'poste',
            'filiales',
            'directions',
            'departements',
            'is_admin',
            'password1', 
            'password2', 
            ]

class EditUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'sexe',
            'email',
            'poste',
            'filiales',
            'directions',
            'departements',
            'is_admin',
            ]