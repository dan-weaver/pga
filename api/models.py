from django.db import models
# Create your models here.

class Golfer(models.Model):
	name = models.CharField(max_length=40)

class Event(models.Model):
	name = models.CharField(max_length=60)
	active = models.BooleanField()

class Result(models.Model):
	event = models.ForeignKey(Event)
	golfer = models.ForeignKey(Golfer, related_name="results")
	income = models.IntegerField()
