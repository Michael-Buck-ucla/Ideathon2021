from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
from .models import Event

# Create your views here.
def home(request):
    event_list = Event.objects.all()
    locations = {}
    
    for event in event_list:
        print(event.name)
        locations[event.name] = {'lat':event.latitude, 'long':event.longitude}
    context = {}
    context['api_key'] = settings.GOOGLE_API_KEY
    # locations = [{'lat' : 32, 'long' : 120}, {'lat' : 29, 'long' : 120}, {'lat' : 34, 'long' : 100}]
    context['locations'] = json.dumps(locations)
    # json.dumps( [{"lat" : 32, "long" : 120}, {"lat" : 29, "long" : 120}])
    return render(request,'home.html', context)