import urllib.request
import json
import time

def raterequest():
    data = urllib.request.urlopen('https://old.bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    ParsedData = json.loads(data.read())
    targetcur = (ParsedData[33]["cc"], str(ParsedData[33]["rate"]), ParsedData[33]["exchangedate"])
    print(" ".join(targetcur))
    time.sleep(5)

try:
    while True:
        raterequest()
except KeyboardInterrupt:
    pass
