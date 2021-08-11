#bot_response
import os
import psycopg2
import datetime

from response import (Response, UrlButton, QuickReply, Gif, Image)

from bot_constants import *
from bot_functions import *
from rive_reply import rive_response

#from TheScrape2 import check_for_dino as get_dino   #for scraping htmls
from TheScrape3 import (get_dino, check_for_day)
from shopen import *                    #for all shopen related
from killswitch import add_custom_message
from calendar1 import get_events
from jokes import get_joke               #for jokes

from users import *                     #for viewing users

#from utils import wit_response
from models import (Sender, GlobalVar)

def bot_response(recipient_id, message_text="", attachment = ""):
	try:
		message = message_text.lower()
		response = Response(recipient_id)
		picture = Response(recipient_id)
		if attachment != "":
			response.text = "Nice pic!"
		elif "dookie:" in message and str(recipient_id) in Admin_ID: #for adding custom messages
			con = getCon()
			add_custom_message(message_text, con)
			response.text = "Adding custom message..."
			con.close()

		elif "time" in message:
			response.text = getTime(message)

		elif check_for_dino(message):
			value = check_for_dino(message)
			con = getCon()
			response.text = get_dino(message, value, recipient_id, con) #CURRENTLY CALLED check_for_dino
			con.close()

			button = UrlButton("Latemeal","https://user.resi.inloop.com.au/home").get_button()
			response.add_button(button)
			button = UrlButton("Leave Feedback","https://bit.ly/3hVT0DX").get_button()
			response.add_button(button)

		elif check_for_shopen(message, recipient_id):
			response.text = check_for_shopen(message, recipient_id)

		elif check_for_calendar(message):
			response.text = check_for_calendar(message)

		elif check_for_day(message) or "tomorrow" in message or "today" in message:
			response.text = get_dino(message, "breakfast", recipient_id)
			response.send()
			response.text = get_dino(message, "lunch", recipient_id)
			response.send()
			response.text = get_dino(message, "dinner", recipient_id)

			button = UrlButton("Latemeal","https://user.resi.inloop.com.au/home").get_button()
			response.add_button(button)

		elif "latemeal" in message or "late" in message or "inloop" in message:
			response = "Order a late meal here:"
			button = UrlButton("Latemeal","https://user.resi.inloop.com.au/home").get_button()
			response.add_button(button)

		elif "idiot" in message or "dumb" in message or "stupid" in message:
			link = Sender(recipient_id).get_profile_pic()
			picture.attachment = Image(link).get_image()
			picture.send()
			response.text = "This you?"

		elif "gif" in message:
			response.attachment = Gif("nice").get_gif()

		elif "joke" in message:
			response.text = get_joke()

		elif "test" == message:
			testy = GlobalVar("test1")
			testy.insert({'index':2,'date':'27-05-21','column1':'hello1','column2':'goodbye1'})
			testy.get()

		elif "show me users" in message:

			if str(recipient_id) in Admin_ID: 
				con = getCon()
				response.text = "Check the logs."
				print("Users: \n" + view_users(con))
				con.close()
			else:
				response.text = "You shall not, PASS: \n" + str(recipient_id)

		# elif "hello" in message or "hey" in message or "help" in message or "hi" in message: #hi sometimes causes conflicts
		# 	button = UrlButton("BssrBot Page","https://www.facebook.com/BssrBot-107323461505853/").get_button()
		# 	response.add_button(button)
		# 	response.text = greeting_message

		elif "thx" in message or "thanks" in message or "thank you" in message or "thankyou" in message:
			response.text =  " ".join(["You're welcome!", u"\U0001F60B"]) #tongue out emoji

		else:	
			try:
				response.text = rive_response(recipient_id, message)
			except:
				response.text = "'".join(["Sorry, I don't understand: ",message_text,""])
				PrintException()
				
		response.add_quick_replies(dino_quickreplies)
		response.send()
	except:
		PrintException()
	return "Response formulated"

def getTime(message):
	# #updated dino times
	# if days_until(datetime.date(2021, 7, 26))<=0:
	# 	global notbassertimes, bassertimes, dinotimes
	# 	notbassertimes = new_notbassertimes
	# 	bassertimes = new_bassertimes
	# 	dinotimes = new_dinotimes

	response = ""
	if "baxter" in message:
		response = response + notbassertimes["Baxter"]
	elif "goldstein" in message or "goldie" in message or "goldy" in message:
		response = response + notbassertimes["Goldstein"]
	elif "fig" in message:
		response = response + notbassertimes["Fig"]
	elif "hall" in message:
		response = response + notbassertimes["Hall"]
	else:
		meal = check_for_dino(message)
		if meal:
			if meal == "dino":
				response = response + dinotimes
			else:
				response = "".join([response, f"Basser {meal} is at ",bassertimes[meal],"."])
		else :
			response = response + dinotimes
	return response


def check_for_dino(message):
	value = None
	if "dino" in message:
		value = "dino"
	elif "breakfast" in message or "breaky" in message or "brekky" in message:
		value = "breakfast"
	elif "lunch" in message:
		value = "lunch"
	elif "dinner" in message or "dins" in message or "supper" in message:
		value = "dinner"
	return value

def check_for_shopen(message, recipient_id): #this can be mademore efficient
	user = Sender(recipient_id)
	name =  user.get_fullname()
	response = ""
	global shop_catalogue
	if shop_catalogue == None:
		#global shop_catalogue
		shop_catalogue = "No catalogue." + u"\U0001F4A9" #poop emoji
	if "i would like to open the shop" in message:
		con = getCon()
		response = response + open_shopen(name, con)
		con.close()
	elif "i would like to close the shop" in message:
		con = getCon()
		##add feature where only person who opened can close
		response = response + close_shopen(name, con)
		con.close()
	elif "shopen" in message or ("shop" in message and ("catalogue" not in message and "sell" not in message)):
		con = getCon()
		response = response + get_shopen(con)
		response = response + "\n" + "\n" + shop_catalogue
		con.close()
	elif "catalogue" in message or ("shop" in message and "sell" in message):
		response = response + str(shop_catalogue)
	return response

def check_for_calendar(message):
	response = ""
	if "events" in message \
	or "event" in message \
	or "whats on" in message \
	or "what’s on" in message \
	or "what's on" in message \
	or "what is on" in message:
		con = getCon()
		response = response + get_events(message, con)
		con.close()
	return response
