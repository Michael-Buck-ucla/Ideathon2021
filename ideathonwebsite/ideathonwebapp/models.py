from django.db import models

# Create your models here.

class Event(models.Model):
	AGE_RANGES = (
        ('AA', 'All Ages'),
        ('18', '18+'),
        ('21', '21+'),
    )
	name = models.CharField(max_length=255)
	address = models.SlugField(unique=True, max_length=255) #need address
	genre = models.CharField(max_length=255)
	startTime = models.DateTimeField(auto_now_add=True)
	endTime = models.DateTimeField(auto_now_add=True)
	host = models.CharField(max_length=255)
	audienceNumber = models.IntegerField()
	entryCost = models.FloatField()
	ageRange = models.CharField(max_length=2, choices=AGE_RANGES)


