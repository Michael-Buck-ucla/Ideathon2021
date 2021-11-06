from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Event(models.Model):
	AGE_RANGES = (
        ('All Ages', 'All Ages'),
        ('18+', '18+'),
        ('21+', '21+'),
    )
	name = models.CharField(max_length=255)
	address = models.SlugField(unique=True, max_length=255) #need address
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	genre = models.CharField(max_length=255)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	host = models.CharField(max_length=255)
	audienceNumber = models.IntegerField()
	entryCost = models.FloatField()
	ageRange = models.CharField(max_length=10, choices=AGE_RANGES)

class Video(models.Model):
	title = models.CharField(max_length=100)
	event = models.CharField(max_length=100)
	video = models.FileField(upload_to='videos/')


