import csv
import requests
from bs4 import BeautifulSoup as bs



url = "http://espn.go.com/golf/leaderboard"


def operation(self, tree):
	mapping = [{"name":"player", "position":3}]
	row = []
	for i in mapping:
		row.append(tree[i['position']].text)
	print row[0]



def scraper(url, op):
	r = requests.get(url)
	soup = bs(r.text)
	table = soup.table
	rows = table.findAll('tr')
	for tr in rows:
		cols = tr.findAll('td')
		if len(cols) > 0:
			op(cols)


if __name__ == '__main__':
	scraper(url, operation)



