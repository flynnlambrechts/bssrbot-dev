def checkfornumber(message):
    if "one" in message or "1" in message:
        weeknumber = 1
    elif "two" in message or "2" in message:
        weeknumber = 2
    elif "three" in message or "3" in message:
        weeknumber = 3
    elif "four" in message or "4" in message:
        weeknumber = 4
    elif "five" in message or "5" in message:
        weeknumber = 5
    elif "six" in message or "6" in message:
        weeknumber = 6
    elif "seven" in message or "7" in message:
        weeknumber = 7
    elif "eight" in message or "8" in message:
        weeknumber = 8
    elif "nine" in message or "9" in message:
        weeknumber = 9
    elif "ten" in message or "10" in message:
        weeknumber = 10
    return weeknumber

message = "week three"
if checkfornumber(message): # checks if user is asking for a specific week
        weekofterm = checkfornumber(message)
        print(weekofterm)
