from django.db.models import Sum
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from api.serializers import GolferSerializer, GolferInputSerializer, EventSerializer, ResultSerializer
from api.models import Golfer, Event, Result

class GolferList(APIView):
	def get(self, request, format=None):
		golfers = Golfer.objects.annotate(prize_money=Sum('results__income'))
		serializer = GolferSerializer(golfers, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = GolferInputSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

class GolferDetail(APIView):
	def get_object(self, pk):
		try:
			return Golfer.objects.annotate(prize_money=Sum('results__income')).get(pk=pk)
		except Golfer.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		golfer = self.get_object(pk)
		serializer = GolferSerializer(golfer)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		golfer = self.get_object(pk)
		serializer = GolferSerializer(golfer, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		golfer = self.get_object(pk)
		golfer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ResultsList(generics.ListCreateAPIView):
	queryset = Result.objects.all()
	serializer_class = ResultSerializer

class ResultsDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Result.objects.all()
	serializer_class = ResultSerializer

class EventsList(generics.ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class EventsDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


