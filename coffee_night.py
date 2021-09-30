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
	date = datetime.datetime.now(TIMEZONE).strftime('%d-%m-%y')

	con = getCon()
	cur = con.cursor()
	cur.execute('''SELECT * FROM %s WHERE ''')
	con.close()
	return 0


#--- Photo Submission
