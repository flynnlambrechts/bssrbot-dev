#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos
import datetime
from bot_constants import TIMEZONE
from bot_functions import (getCon, PrintException)

from models import Sender

# Getting qutoes or wildcat nominations
# Inputing into here is done through rive_reply.py
def get_coffee(item): #item is either quotes or wildcats
	try:
		date = datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d')

		con = getCon()
		cur = con.cursor()
		cur.execute('''SELECT * FROM wildcats WHERE date >= '2021-09-29'::DATE''') #change this to the previous coffee night
		
		rows = cur.fetchall()
		for row in rows:
			print(row)
			# for i in row:
			# 	print(row[i])
			# 	print(" ")
			print("\n")

		con.close()
	except:
		PrintException()
	return 0


#--- Photo Submission
