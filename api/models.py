from django.db import models
# Create your models here.

class Golfer(models.Model):
	first_name = models.CharField(max_length=10)
	last_name = models.CharField(max_length=10)

class Event(models.Model):
	name = models.CharField(max_length=60)
	active = models.BooleanField()

class Result(models.Model):
	event = models.ForeignKey(Event)
	golfer = models.ForeignKey(Golfer, related_name="results")
	income = models.IntegerField()
