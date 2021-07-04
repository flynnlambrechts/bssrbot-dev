from pytz import timezone
import datetime

def getmenuweek():
    TIMEZONE = timezone('Australia/Sydney')
    x = datetime.datetime.now(TIMEZONE)
    week = (int(x.strftime("%W"))+1) #plus one changes the cycle to match the dino cycle
    menuweek = (week)%4+1 #this cheeky +1 changes range from (0-3 to 1-4)
    print(menuweek)
    return menuweek

def checkForDay(message): #check of day of week specified
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
    return day

# def checkForDay(message): #check of day of week specified
#     days = {"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
#     for i in range(len(days)):
#         print(i)
#     return day
