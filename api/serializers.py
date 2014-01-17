from rest_framework import serializers

from api.models import Golfer, Event, Result



class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('name',  'id', 'active')


class ResultSerializer(serializers.ModelSerializer):
	golfer = serializers.Field(source='golfer.first_name')
	class Meta:
		model = Result
		fields = ('income', 'golfer', 'id', 'event')

class GolferSerializer(serializers.ModelSerializer):
	prize_money = serializers.IntegerField(required=False)
	class Meta:
		model = Golfer
		fields = ('name', 'id', 'prize_money')

class GolferInputSerializer(serializers.ModelSerializer):
	# results = serializers.SlugRelatedField(many=True, slug_field='income')
	class Meta:
		model = Golfer
		fields = ('name', 'id')