#Calendar
from datetime import *
import time

from pytz import timezone
TIMEZONE = timezone('Australia/Sydney')

from TheScrape3 import check_for_day
from bot_constants import week_days
from bot_functions import PrintException

def getDay(message):
    current_day = datetime.now(TIMEZONE).weekday()
    x = datetime.now(TIMEZONE)
    weekofterm = (int(x.strftime("%W"))-21) #ZERO WEEK HERE
    
    day = "Today"
    column_value = int(current_day) + 2
    
    if "tomorrow" in message or "tmrw" in message or "tomoz" in message:
        day = "Tomorrow"
        #print(current_day)
        if int(current_day) == 6: #if sunday
            weekofterm+=1
            column_value = 2 #sets column to monday the next week
        else:
            column_value = int(current_day) + 3
        #print(column_value)
    elif check_for_day(message):
        print("day found")
        #global week_days
        if current_day > int(check_for_day(message)):
            if weekofterm == 10:
                print("end of term") #FIX this
            else:
                weekofterm+=1
            current_day = int(check_for_day(message))
            column_value = current_day + 2
            day = str(week_days[int(check_for_day(message))])
        else:
            current_day = int(check_for_day(message))
            column_value = current_day + 2
            day = str(week_days[int(check_for_day(message))])
    return current_day, day, weekofterm, column_value

def check_for_number(message):
    weeknumber = ""
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

###COLUMNS:
##0 - week
##1 - wholeweek
##2 - monday
##3 - tuesday
##4 - wednesday
##5 - thursday
##6 - friday
##7 - saturday
##8 - sunday
def get_events(message, con):
    response  = ""
    # global weekofterm
    # global column_value
    # global day
    try:
        current_day, day, weekofterm, column_value = getDay(message)
        if "week" in message:
            cur  = con.cursor()
            getDay(message)
            if check_for_number(message): # checks if user is asking for a specific week
                weekofterm = check_for_number(message)
            if "next" in message:
                weekofterm+=1
            cur.execute('''SELECT * FROM calendar WHERE week = %s''',str(weekofterm))
            row = cur.fetchone()
            headers = ["Whole Week: ","Monday: ", "Tuesday: ", "Wednesday: ", "Thursday: ", "Friday:  " ,"Saturday: ", "Sunday: "]
            response = response + f"Events in Week {weekofterm}:\n"
            for i in range(1,9):
                if str(row[i]) == "None": ### THIS WILL ALSO NEED TO BE CHANGED
                    response = response + headers[i-1] + "No Events" + "\n\n"
                else:
                    response = response + headers[i-1] + row[i] + "\n\n"
        else:
            row = []
            cur  = con.cursor()
            getDay(message)
            cur.execute('''SELECT * FROM calendar WHERE week = %s''',str(weekofterm))
            row = cur.fetchone()
            #print(str(row) + "- ROW THING")
            #print(str(weekofterm) + " week")
            if str(row[column_value]) == "None": #this can be changed to "is None" next time
                response = f"No events on {day}."
            else:
                response = response + f"Events on {day}: \n" + str(row[column_value])
             
    except Exception as error:
        #PrintException()
        #response = response + "Error in getting events: \n" + str(error)
        response = response + "It's Holidays go have fun."
    return response
    
