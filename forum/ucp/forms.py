from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import password_validation

class CustomUserCreationForm(UserCreationForm):
     username = forms.CharField(
        label=(""),
        widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"}),
    )
     email = forms.CharField(
        label=(""),
        widget=forms.TextInput(attrs={"placeholder": "Почта"}),
    )
     password1 = forms.CharField(
        label=(""),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Пароль"}),
        help_text= ''
    )
     password2 = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Повторите пароль"}),
        strip=False,
    )
     class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        
class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        label=(""),
        widget=forms.TextInput(attrs={"placeholder": "Имя пользователя"}),
    )
    
    password = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}),
        )
        
