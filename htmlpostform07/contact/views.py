from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def contact_form(request):
    return render(request, 'contact.html')
