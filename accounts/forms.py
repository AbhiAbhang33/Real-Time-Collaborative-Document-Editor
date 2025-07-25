from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })
    )
