from datetime import *
from pytz import timezone
TIMEZONE = timezone('Australia/Sydney')

def daysuntil(future): #date provided in date(YYYY,M,D) format
    # today = date.today()
    today = datetime.now(TIMEZONE)
    today = int(today.strftime('%j'))
    print(type(int(today)))
    diff = int(future.strftime('%j')) - today
    return diff

# day = date(2021,9,13)
# print(daysuntil(day))

# day = date(2021, 9, 13)
# if date.today() <= day:
# 	print(True)
# else:
# 	print(False)


# current_day = datetime.now(TIMEZONE).weekday()
# print(current_day.date())

# row = "2021-07-17 07:57:57.759856"
# time = datetime.datetime.strptime(row, '%Y-%m-%d %H:%M:%S.%f')
# time = time.strftime('%I:%M%p %d %b')
# print(time)


day = "Today"
if day == "Today":
			future = date(2021, 9, 13)
			if date.today() <= future:
				response = " ".join([str(daysuntil(future)), "Days until TRI 3..."])
			else:
				print(False)
				response = "nope"

print(response)