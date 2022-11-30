from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView


def home_page(request):
    return render(request, 'index.html')

def sign_in_page(request):
    return render(request, 'sign_in.html')
class SignInView(LoginView):
    form_class = CustomAuthForm
    template_name = 'sign_in.html'
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('home')

