from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Registration
from django import forms


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


class Usercreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
