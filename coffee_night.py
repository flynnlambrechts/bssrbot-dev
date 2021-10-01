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
		#print(start_date)

		con = getCon()
		cur = con.cursor()
		cur.execute(f'''SELECT * FROM {item} WHERE date >= '{start_date}'::DATE''') #change this to the previous coffee night
		rows = cur.fetchall()

		#f = open(f"coffee_{item}_{date}.txt", "w+")
		result = f"{date} --- {item}\n"

		with open(f"coffee_{item}_{date}.txt", "w+") as f:
			for row in rows:
				result = result + f"{row[0]} | {row[1]} | {row[2]} | {row[3]}\n"
				print(row)

		f.close()
		con.close()
	except:
		PrintException()
	return result


#--- Photo Submission
