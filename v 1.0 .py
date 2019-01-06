import urllib.request
import json
import time

def repeat():
    data = urllib.request.urlopen('http://resources.finance.ua/ru/public/currency-cash.json')
    ParsedData = json.loads(data.read())
    print(ParsedData["organizations"][0]["currencies"]["EUR"])
    time.sleep(5)

while True:
	repeat()
	
    