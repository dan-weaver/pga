from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from api.models import Golfer, Event
import scraper

golfers = []

def scraper_op(tree):
		mapping = [{"name":"player", "position":3}]
		row = []
		for i in mapping:
			row.append(tree[i['position']].text)
		golfers.append(row[0])

class Command(BaseCommand):
	help = 'Creates a PGA Event and populates any golfers that are not already in database'
	args = '<url url ...>'
	option_list = BaseCommand.option_list + (
		make_option('--url',
			default='http://espn.go.com/golf/leaderboard'
			),
		)
	def handle(self, *args, **options):
		
		url = options['url']
		
		scraper.scraper(url, scraper_op)

		for i in golfers:
			# print first
			try:
				g = Golfer.objects.get(name=i)
			except Golfer.DoesNotExist:
				print i + " does not exist. Creating..."
				g = Golfer(name=i)
				g.save()

		name = raw_input('Name of event?: ')
		event = Event(name=name, active=True)
		event.save()

