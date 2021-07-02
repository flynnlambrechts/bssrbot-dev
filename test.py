from pytz import timezone
import datetime

def getmenuweek():
    TIMEZONE = timezone('Australia/Sydney')
    x = datetime.datetime.now(TIMEZONE)
    week = (int(x.strftime("%W"))+1) 
    print((week)%4+1) #cheeky factor of 1 changes range from (0-3 to 1-4)
    return week

getmenuweek()
