from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PlayersForm
from django.views.generic.edit import CreateView


def home_page(request):
    return render(request, 'index.html')

def sign_in_page(request):
    return render(request, 'sign_in.html')

def sign_up_page(request):
    return render(request, 'sign_up.html')
class SignUpView(CreateView):
    form_class = PlayersForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('home')

