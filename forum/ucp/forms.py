from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
        help_text=password_validation.password_validators_help_text_html()
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
        
        
