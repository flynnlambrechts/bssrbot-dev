#Calendar
from datetime import *
import time

import pytz
TIMEZONE = pytz.timezone('Australia/Sydney')

from getmenuweek import checkForDay

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#column_value = 0
'''
def getevent(day, message):
    global week_days
    current_day = datetime.now(TIMEZONE).weekday()
    if "tomorrow" in message or "tmrw" in message or "tomoz" in message:

    elif 
'''


def getDay(message):
    global current_day
    
    global weekofterm
    global column_value
    global day

    current_day = datetime.now(TIMEZONE).weekday()
    x = datetime.now(TIMEZONE)
    weekofterm = (int(x.strftime("%W"))-20) #ZERO WEEK HERE
    
    day = "Today"
    column_value = int(current_day) + 2
    
    if "tomorrow" in message or "tmrw" in message or "tomoz" in message:
        day = "Tomorrow"
        print(current_day)
        if int(current_day) == 6: #if sunday
            weekofterm+=1
            column_value = 2 #sets column to monday the next week
        else:
            column_value = int(current_day) + 3
        print(column_value)
    elif "week" in message: #add for next week or week number
        day = "This week"
        column_value = 1
        #add for each day
    elif checkForDay(message):
        print("day found")
        global week_days
        if current_day > int(checkForDay(message)):
            if weekofterm == 10:
                print("end of term") #FIX this
            else:
                weekofterm+=1
            current_day = int(checkForDay(message))
            column_value = current_day + 2
            day = str(week_days[int(checkForDay(message))])
        else:
            current_day = int(checkForDay(message))
            column_value = current_day + 2
            day = str(week_days[int(checkForDay(message))])
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
    global weekofterm
    global column_value
    global day
##    try:
    row = []
    cur  = con.cursor()
    getDay(message)
    cur.execute('''SELECT * FROM calendar WHERE week = %s''',str(weekofterm))
    row = cur.fetchone()
    print(str(row) + "- ROW THING")
    print(str(weekofterm) + " week")
    if str(row[column_value]) == "null": #this can be changed to "is None" next time
        response = f"No events on {day}."
    else:
        response = response + f"Events on {day}: \n" + str(row[column_value])
         
##    except Exception as error:
##        print("Error: " + str(error) + "\n" + str(type(error)))
##        response = response + "Error in getting events: \n" + str(error)
    return response
    
