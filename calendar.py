#Calendar

week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def checkForCalendar(message):
    response = ""
    if "events" in message
    or "event" in message
    or "what's on" in message
    or "whats on" in message
    or "what is on" in message:
        response = response + "Events are: \n"
        
    return response
        
'''
def getevent(day, message):
    global week_days
    current_day = datetime.now(TIMEZONE).weekday()
    if "tomorrow" in message or "tmrw" in message or "tomoz" in message:

    elif 
'''


    
    
