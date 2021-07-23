import datetime
from pytz import timezone

TIMEZONE = timezone('Australia/Sydney')

def daysuntil(future): #date provided in date(YYYY,M,D) format
    today = int(datetime.datetime.now(TIMEZONE).strftime('%j'))
    return int(future.strftime('%j')) - today

future = datetime.date(2021, 7, 26)
if daysuntil(future) > 0:
	print(True)
else:
	print(False)