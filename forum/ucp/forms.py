from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Players

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        
        
class PlayersForm(forms.ModelForm):
    nameuser = forms.CharField(max_length=100)
    emailuser = forms.EmailField(max_length=100)
    password_one = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Players
        fields = '__all__'