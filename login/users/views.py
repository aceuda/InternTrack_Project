from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')

def about(request):
    return render(request, 'users/about.html')

# Create your views here.
