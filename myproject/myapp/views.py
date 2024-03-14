from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def add_elements(request):
    return render(request, 'add.html')