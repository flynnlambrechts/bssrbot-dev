#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos
import datetime
from dateutil.relativedelta import relativedelta, WE
from tabulate import tabulate
from github import Github

from bot_constants import (TIMEZONE, PAT)
from bot_functions import (getCon, PrintException)

from models import Sender

# https://medium.com/geekculture/files-on-heroku-cd09509ed285
github = Github(PAT)
repository = github.get_user().get_repo('bssrbot3') #maybe make so this knows whether its in bssrbot or bssrbot-dev

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

		# path in the repository
		filename = 'coffee.html'

		#f = open(f"coffee_{item}_{date}.txt", "w+")
		result = f"{date} --- {item}\n"
		table = []
		for row in rows:
			table.append(list(row))
			result = result + f"{row[0]} | {row[1]} | {row[2]} | {row[3]}\n"
			print(row)

		content = tabulate(table, tablefmt='html')

		con.close()

		# create with commit message
		f = repository.create_file(filename, "Coffee Night", content)

	except:
		PrintException()
	return result


#--- Photo Submission
