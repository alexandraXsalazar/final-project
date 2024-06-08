from django.shortcuts import render
from .models import Bug

def home(request):
    bugs = Bug.objects.all()
    return render(request, 'home.html', {'bugs': bugs})
