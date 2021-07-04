import time

def checkForDay(message): #check of day of week specified
	start = time.time()
	days = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
	for key, value in days.items():
		print(key)
		print(value)
		if key in message:
			day = value
			break
		else:
			day = ""
	end = time.time()
	print(end - start)
	return day

message = "breakfast saturday"
print(str(checkForDay(message)) + " Result")

def checkDay(message): #check of day of week specified
	start = time.time()
	day = ""
	if "monday" in message or " mon" in message or "mon " in message:
	    day = str('0')
	elif "tuesday" in message or " tues" in message or "tues " in message:
	    day = 1
	elif "wednesday" in message or " wed" in message or "wed " in message:
	    day = 2 
	elif "thursday" in message or " thur" in message or "thur " in message or " thurs" in message or "thurs " in message:
	    day = 3
	elif "friday" in message or " fri" in message or "fri " in message:
	    day = 4
	elif "saturday" in message or " sat" in message or "sat " in message:
	    day = 5
	elif "sunday" in message or " sun" in message or "sun " in message:
	    day = 6
	end = time.time()
	print(end - start)
	return day

print(str(checkDay(message)) + " Result")