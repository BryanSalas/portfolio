from datetime import datetime

from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow()})

def bio(request) :
    return render(request, 'bio.html')

def projects(request) :
    return render(request, 'projects.html')

def contact(request) :
    return render(request, 'contact.html')
