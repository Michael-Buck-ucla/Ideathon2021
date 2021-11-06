from django import forms
from .models import Event

class Filter(forms.Form):
    events = Event.objects.all()

    genreChoices = [('','select')]
    genrelist = list( events.values_list('genre', flat=True))
    for item in genrelist:
        genreChoices.append( (str(item),str(item)) )

    startTimeChoices = [('','select')]
    startTimelist = list(events.values_list('startTime', flat=True))
    for item in startTimelist:
        startTimeChoices.append( (str(item),str(item)) )

    endTimeChoices = [('','select')]
    endTimelist = list( events.values_list('endTime', flat=True))
    for item in endTimelist:
        endTimeChoices.append( (str(item),str(item)) )

    entryCostChoices = [('','select')]
    entryCostlist = list( events.values_list('entryCost', flat=True))
    for item in entryCostlist:
        entryCostChoices.append( (str(item),str(item)) )

    ageRangeChoices = [('','select')]
    ageRangelist = list( events.values_list('ageRange', flat=True))
    for item in ageRangelist:
        ageRangeChoices.append( (str(item),str(item)) )

    genre = forms.ChoiceField(label = "Genre", required = False, choices = genreChoices)
    startTime = forms.ChoiceField(label = "Start Time", required = False, choices = startTimeChoices)
    endTime = forms.ChoiceField(label = "End Time", required = False, choices = endTimeChoices)
    entryCost = forms.ChoiceField(label = "Entry Cost", required = False, choices = entryCostChoices)
    ageRange = forms.ChoiceField(label = "Age Range", required = False, choices = ageRangeChoices)