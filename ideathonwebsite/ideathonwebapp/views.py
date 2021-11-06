from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
from .models import Event
from .forms import Filter

# Create your views here.
def home(request):
    context = {}
    event_list = Event.objects.all()
    locations = {}
    context['form'] = Filter()

    print(event_list)
    if request.method == "GET":
        form = Filter(request.GET)
        print('Get')
        if form.is_valid():
            print("valid")
            filters = form.cleaned_data
            if filters['genre'] != '':
                event_list = event_list.filter(genre=filters['genre'])

            if filters['startTime'] != '':
                event_list = event_list.filter(startTime=filters['startTime'])

            if filters['endTime'] != '':
                event_list = event_list.filter(endTime=filters['endTime'])

            if filters['entryCost'] != '':
                event_list = event_list.filter(entryCost=filters['entryCost'])

            
            if filters['ageRange'] != '':
                event_list = event_list.filter(ageRange=filters['ageRange'])




            print(filters)
    print(event_list)
    context['events'] = event_list




    for event in event_list:
        locations[event.name] = {'lat':event.latitude, 'long':event.longitude, 'genre':event.genre, 'start':str(event.startTime), 'end':str(event.endTime), 'host':event.host, 'num':event.audienceNumber, 'cost':event.entryCost, 'age':event.ageRange}
        
    context['api_key'] = settings.GOOGLE_API_KEY
    # locations = [{'lat' : 32, 'long' : 120}, {'lat' : 29, 'long' : 120}, {'lat' : 34, 'long' : 100}]
    context['locations'] = json.dumps(locations)
    # json.dumps( [{"lat" : 32, "long" : 120}, {"lat" : 29, "long" : 120}])
    return render(request,'home.html', context)


