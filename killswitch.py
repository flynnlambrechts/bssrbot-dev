##custom message
import psycopg2

import time
import datetime
from pytz import timezone

#command example dookie: meal "message"
import re

index = "1"
TIMEZONE = timezone('Australia/Sydney')

def get_custom_message(message):
	try:
		custom_message = re.search("<(.+?)>", message).group(1)
	except AttributeError:
		custom_message = "no message"
		print('no message found')
	return custom_message
message = "dookie: dinner ‘dino changed it up but heres what it was supposed to be‘"
#print(get_custom_message(message))



def add_custom_message(message, con):
	#insert new row if new day
	#update current day if same day
	custom_message = get_custom_message(message)
	print(custom_message)
	breakfast = None
	lunch = None
	dinner = None
	allday = None

	if "breakfast" in message:
		breakfast = custom_message
	elif "lunch" in message:
		lunch = custom_message
	elif "dinner" in message:
		dinner = custom_message
	elif "all" in message:
		allday = custom_message
	else:
		print("no meal specified")

	try:
		date = str(datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d'))
		cur = con.cursor()

		cur.execute('''SELECT day FROM custom_message WHERE day = %s''', (date,))
			#check if current day exists
		
		dummy = str(cur.fetchone())
		print(dummy + "dummy")

		if dummy is not None: #if the day exits then update current day
			print("updating row")
			#make so only updates specific row instead of all rows
			cur.execute('''UPDATE custom_message SET
			allday = COALESCE(%s,allday), breakfast = COALESCE(%s,breakfast), lunch = COALESCE(%s,lunch),
			dinner = COALESCE(%s,dinner)
			WHERE day = %s''', (allday,breakfast,lunch,dinner,date,))
			con.commit()
			print("custom_message updated successfully")
		else: #otherwise add new row with the current date
			print("adding row")
			cur.execute('''INSERT INTO custom_message(
				day, allday, breakfast, lunch, dinner)
				VALUES (%s,%s,%s,%s,%s)''', 
				(date,allday,breakfast,lunch,dinner,))
			con.commit()
			print("row added successfully")


	except Exception as error:
		print("Error in add_custom_message: " + str(error) + "\n" + str(type(error)))
	return "success"









