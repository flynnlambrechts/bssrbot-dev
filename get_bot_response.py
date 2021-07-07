#get_bot_response
import os
import psycopg2 

from response import (Response, UrlButton, QuickReply, Gif)
from shop_catalogue import shop_catalogue
from TheScrape2 import dinotimes

from TheScrape2 import checkForDino as getDino   #for scraping htmls
from TheScrape2 import dinotimes        #pulls the dino times from the scrape
from TheScrape2 import checkForButton   #Checks whether should add feedback button
from EasterEggs import checkForEasterEggs #self explanatory
from shopen import *                    #for all shopen related
from killswitch import add_custom_message
from calendar1 import get_events
from jokes import getjoke               #for jokes
from shop_catalogue import shop_catalogue 
from otherdinotimes import notBasser

from users import *                     #for viewing users
from getmenuweek import checkForDay

from models import Sender

###MAKE ALL INTO INDIVDUAL FUNCTIONS THAT HANDLE TO OCCURANCES
###Add buttons and send using response.py

def getCon(): #gets the connection  to the database when required
    if "HEROKU" in os.environ:
        DATABASE_URL =  os.environ['DATABASE_URL']
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
    else:
        con = psycopg2.connect(database="bssrbot1", user="flynnlambrechts", password="", host="127.0.0.1", port="5432")
        print("Local Database opened successfully")
    return con


def get_bot_response(message_text, recipient_id):
   
    message = message_text.lower()

    if "dookie:" in message and str(recipient_id) in Admin_ID: #for adding custom messages
        con = getCon()
        add_custom_message(message, con)
        response.text = "Adding custom message..."
        con.close()

    elif notBasser(message):
        response.text = notBasser(message)

    elif checkForDino(message): #rename to checkfordino later
        meal = checkForDino(message)
        con = getCon()
        response.text = getDino(message, con, value) #CURRENTLY CALLED checkForDino
        con.close()
        button = UrlButton("Latemeal","https://user.resi.inloop.com.au/home")
        response.add_button(button)
        button = UrlButton("Leave Feedback","https://bit.ly/3hVT0DX")
        response.add_button(button)
        

    elif "hello" in message or "hey" in message or "help" in message or "hi" in message:
    	greeting_message = f"Hello! Welcome to the BssrBot! I'm here to help you with all your dino and calendar needs.\
    			Here are some example questions:\
    			\n1. What's for dino? \
    			\n2. What's for lunch today? \
    			\n3. Is shopen? \
    			\n4. What's the shop catalogue? \
    			\n5. What's on tonight? \
    			\n6. Events on this week?"
    	button = UrlButton("BssrBot Page","https://www.facebook.com/BssrBot-107323461505853/")
        response.text = greeting_message
        response.add_button(button)

    elif "thx" in message or "thanks" in message or "thank you" in message or "thankyou" in message:
        response.text =  " ".join(["You're welcome!", u"\U0001F60B"]) #tongue out emoji

    elif checkForShopen(message, recipient_id):
        response.text = checkForShopen(message, recipient_id)

    elif checkForCalendar(message):
        response.text = checkForCalendar(message)

    elif checkForEasterEggs(message):
        response.text = checkForEasterEggs(message)

    elif checkForDay(message) or "tomorrow" in message or "today" in message:
        response.text = "Blank for now..."
        button = UrlButton("Latemeal","https://user.resi.inloop.com.au/home")
        response.add_button(button)

    elif "time" in message:
        response.text = dinotimes

    elif "latemeal" in message or "late" in message or "inloop" in message:
        response = "Order a late meal here:"
        button = UrlButton("Latemeal","https://user.resi.inloop.com.au/home")
        response.add_button(button)

    elif "my name" in message:
        user = Sender(recipient_id)
        response.text = user.get_fullname()

    elif "gif" in message:
        response.attachment = Gif("nice").get_gif()

    elif "joke" in message:
        response.text = getjoke()

    elif "show me users" in message:
        
        if str(recipient_id) in Admin_ID: 
        	con = getCon()
        	response.text = "Check the logs."
            print("Users: \n" + view_users(con))
            con.close()
        else:
            response.text = "You shall not, PASS: \n" + str(recipient_id)
    else:
        response.text = "'".join(["Sorry, I don't understand: \n","",message_text,""])
    response.send(recipient_id)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
    return "Response formulated"

def checkForDino(message):
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

def checkForShopen(message, recipient_id):
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

def checkForCalendar(message):
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
