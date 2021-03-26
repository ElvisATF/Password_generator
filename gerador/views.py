from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'gerador/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvxyz')

    if request.GET.get('upercase'):    
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    if request.GET.get('special'): 
        characters.extend(list('!@#$%^*()'))
    if request.GET.get('numbers'): 
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'gerador/password.html', {'password':thepassword})

def about(request):
    return render(request, 'gerador/about.html')