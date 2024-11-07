from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def skills(request):
    return render(request, 'skills.html')