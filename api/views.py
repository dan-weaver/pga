from rest_framework import viewsets
from django.db.models import Sum

from api.serializers import GolferSerializer, GolferInputSerializer, EventSerializer, ResultSerializer
from api.models import Golfer, Event, Result

class GolferViewSet(viewsets.ModelViewSet):
	model = Golfer
	serializer_class = GolferSerializer
	def get_serializer_class(self):
		if self.request.method == 'GET':
			return GolferSerializer
		return GolferInputSerializer
	def get_queryset(self):
		if self.request.method == 'GET':
			return Golfer.objects.annotate(prize_money=Sum('results__income'))
		return Golfer.objects.all()

class ResultViewSet(viewsets.ModelViewSet):
	queryset = Result.objects.all()
	serializer_class = ResultSerializer

class EventViewSet(viewsets.ModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer