from datetime import *

def daysuntil(day): #date provided in date(YYYY,M,D) format
    today = date.today()
    diff = day - today
    return (diff.days)

# day = date(2021,9,13)
# print(daysuntil(day))

day = date(2021, 9, 13)
if date.today() <= day:
	print(True)
else:
	print(False)