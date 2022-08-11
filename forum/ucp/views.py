from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')

def sign_in_page(request):
    return render(request, 'sign_in.html')

def sign_up_page(request):
    return render(request, 'sign_up.html')

