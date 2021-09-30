#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos
import datetime
from bot_constants import TIMEZONE
from bot_functions import getCon

from models import Sender

# Getting qutoes or wildcat nominations
# Inputing into here is done through rive_reply.py
def get_coffee(item): #item is either quotes or wildcats
	date = datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d')

	con = getCon()
	cur = con.cursor()
	cur.execute('''SELECT * FROM %s WHERE date >= "2021-09-29"::DATE''', (item))
	
	rows = cur.fetchall()
	for row in rows:
		for i in row:
			print(row[i])
			print(" ")
		print("\n")

	con.close()

	return 0


#--- Photo Submission
