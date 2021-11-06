from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json
from .models import Event, Video
from .forms import Filter, CreateUserForm

# Create your views here.
def home(request):
    context = {}
    event_list = Event.objects.all()
    locations = {}
    context['form'] = Filter()
    eventtitle = ''

    print(request.GET)
    if 'eventtitle' in request.GET:
        eventtitle = request.GET.get('eventtitle')

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
    print(event_list)
    for event in event_list:
        locations[event.name] = {'lat':event.latitude, 'long':event.longitude, 'genre':event.genre, 'start':str(event.startTime), 'end':str(event.endTime), 'host':event.host, 'num':event.audienceNumber, 'cost':event.entryCost, 'age':event.ageRange}
    if event_list.filter(name = eventtitle):
        context['spotlight'] = event_list.filter(name = eventtitle)[0]
    context['spotlight_distance'] = ''
    if 'distance' in request.GET:
        context['spotlight_distance'] = request.GET.get('distance')
        print(request.GET.get('distance'))
    

    videos = Video.objects.all()
    context['videos'] = videos.filter(event = eventtitle)

    # for event in event_list:
    #     locations[event.name] = {'lat':event.latitude, 'long':event.longitude, 'genre':event.genre, 'start':str(event.startTime), 'end':str(event.endTime), 'host':event.host, 'num':event.audienceNumber, 'cost':event.entryCost, 'age':event.ageRange}

    context['api_key'] = settings.GOOGLE_API_KEY
    # locations = [{'lat' : 32, 'long' : 120}, {'lat' : 29, 'long' : 120}, {'lat' : 34, 'long' : 100}]
    context['locations'] = json.dumps(locations)
    # json.dumps( [{"lat" : 32, "long" : 120}, {"lat" : 29, "long" : 120}])
    return render(request,'home.html', context)

def registerPage(request):
    context = {}
    context['form'] = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request,'register.html', context)

def display(request):
    context = {}
    videos = Video.objects.all()
    context['videos'] = videos
    return render(request,'home.html', context)

