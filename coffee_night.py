#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos
import datetime
from dateutil.relativedelta import relativedelta, WE

from bot_constants import TIMEZONE
from bot_functions import (getCon, PrintException)

from models import Sender

# Getting qutoes or wildcat nominations
# Inputing into here is done through rive_reply.py
def get_coffee(item): #item is either quotes or wildcats
	try:
		date = datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d')
		start_date = datetime.datetime.now(TIMEZONE) + relativedelta(weekday=WE(-1)) #Finds date of last coffee night (assuming it's wednesday)
		print(start_date)
		con = getCon()
		cur = con.cursor()
		cur.execute(f'''SELECT * FROM {item} WHERE date >= '{start_date}'::DATE''') #change this to the previous coffee night
		
		rows = cur.fetchall()
		for row in rows:
			
			print(row)


		con.close()
	except:
		PrintException()
	return 0


#--- Photo Submission
