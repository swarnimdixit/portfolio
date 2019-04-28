from django.shortcuts import render
from .models import blog

def blogpost(request):
    return render(request,'home.html')
