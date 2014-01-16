import csv
import sqlite3
import json

conn =sqlite3.connect('../tmp.db')
c = conn.cursor()
# c.execute("Select * From api_golfer")
print c.fetchone()
out = open('../api/fixtures/golfers.json', 'w')
with open('golfers.txt') as f:
	reader = csv.reader(f, delimiter=',')
	counter=1
	golfers = []
	for i in reader:
		print i
		first = i[0].split(" ")[0]
		last = i[0].split(" ")[1]
		print first, last
		golfer = {
					"model": "api.golfer",
					"pk": None,
					"fields":{
						"first_name": first,
						"last_name": last
					}
				}
		golfers.append(golfer)
	golfer_string = json.dumps(golfers, sort_keys=True, indent=4, separators=(',',':'))
	out.write(golfer_string)

		
