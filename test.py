from datetime import *
from pytz import timezone
TIMEZONE = timezone('Australia/Sydney')

def daysuntil(day): #date provided in date(YYYY,M,D) format
    today = date.today()
    diff = day - today
    return (diff.days)

# day = date(2021,9,13)
# print(daysuntil(day))

# day = date(2021, 9, 13)
# if date.today() <= day:
# 	print(True)
# else:
# 	print(False)


# current_day = datetime.now(TIMEZONE).weekday()
# print(current_day.date())

time_now = datetime.now(TIMEZONE).timestamp()
print(time_now)