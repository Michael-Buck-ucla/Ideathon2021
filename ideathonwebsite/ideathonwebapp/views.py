from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def home(request):
    context = {}
    context['api_key'] = settings.GOOGLE_API_KEY
    return render(request,'home.html', context)