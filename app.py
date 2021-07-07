  
#Python libraries that we need to import for our bot

import os, sys                          #for heroku env
from datetime import *                  #for time proccessing
#import random                           #for random generation
import time                             #for time
#import calendar                        #not neccessary
import pytz                             #timezone
import psycopg2                         #database stuff
import requests                         #for sending get request
import json

from flask import Flask, request        #flask
#from pymessenger.bot import Bot        #library for sending messages no longer used

#from utils import wit_response          #for nlp
from TheScrape2 import checkForDino     #for scraping htmls
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
import response
from get_bot_response import get_bot_response

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN'] #used for fb connection
VERIFY_TOKEN = os.environ['VERIFY_TOKEN'] #used to verify fb
Admin_ID = ["4409117335852974", #Flynn-DEV
            "3760608700732342" #Flynn-REAL
            ] #id of users with powerful permission

TIMEZONE = pytz.timezone('Australia/Sydney') #sets timezone

#Developer: Flynn
#Contributors: Ethan, Jas, Zoe


def getCon(): #gets the connection  to the database when required
    if "HEROKU" in os.environ:
        DATABASE_URL =  os.environ['DATABASE_URL']
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
    else:
        con = psycopg2.connect(database="bssrbot1", user="flynnlambrechts", password="", host="127.0.0.1", port="5432")
        print("Local Database opened successfully")
    return con


#----------------------------------------------------------------------------------------------


#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
#try:
    #log(output) #entire output good for finding sender ids what message contains etc
    for event in output['entry']:
        messaging = event['messaging']
        for message in messaging:
            recipient_id = message['sender']['id']
            if message.get('message'):
                message_text = message['message']['text']
                print(message_text)
                get_bot_response(message_text, recipient_id)
            # else:
            #     print("no message")

# except TypeError: #if anti-idling add on pings bot we wont get an error
#         print('PING!')
# except:
#         print("an error occured...") 
    return "Message Processed"


def log(message):
    print(message)
    sys.stdout.flush()
    
def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def adduser(con, recipient_id): #adds user to DB
    full_name, first_name, last_name, PSID = getdetails(recipient_id)
    insert_user(full_name, first_name, last_name, PSID, con)
    



#formerly uses PyMessenger to send response to user
#now routes to send message with or without buttons
def send_message(recipient_id, response, buttons): #decides what type of respones to send
    if recipient_id == "5443690809005509": #CHECKS IF HUGO IS MESSAGING
        response = response + "\n\nSHUTUP HUGO"
    #sends user the text message provided via input response parameter
    if buttons != []:
        #text = str(response)
        #bot.send_button_message(recipient_id, text, url_button)
        send_buttons(recipient_id, response, buttons)
    elif response == "gif":
        message = "nice"
        send_gif_message(recipient_id, message)
    else:
        #bot.send_text_message(recipient_id, response)
        send_nonbuttons(recipient_id, response)
    con = getCon()
    adduser(con, recipient_id)
    con.close()
    return "success"


#sends response with quick replies and button
def send_buttons(recipient_id, response, buttons): #change to send button message
    params = {
           "access_token": os.environ["ACCESS_TOKEN"]
    }

    headers = {
            "Content-Type": "application/json"
    }
    #message_text = str(response)
    # buttons = [{
    #             "type": "web_url",
    #             "url": "https://bit.ly/3hVT0DX",
    #             "title": "Leave Feedback"
    #             },
    #             {
    #             "type": "web_url",
    #             "url": "https://user.resi.inloop.com.au/home",
    #             "title": "Latemeal"
    #             }
    #             ]
    #print(type(buttons))
    data = json.dumps({
                "recipient": {
                    "id": recipient_id
                },
                "message": {
                    "attachment":{
                        "type":"template",
                        "payload":{
                            "template_type":"button",
                            "text":str(response),
                            "buttons": buttons
                        }
                    },
                    "quick_replies":[{
                            "content_type":"text",
                            "title":"Breakfast",
                            "payload":"Breakfast"
                            },
                            {
                            "content_type":"text",
                            "title":"Lunch",
                            "payload":"Lunch"
                            },
                            {
                            "content_type":"text",
                            "title":"Dinner",
                            "payload":"Dinner"
                            },
                            {
                            "content_type":"text",
                            "title":"Dino",
                            "payload":"Dino"
                            }]
                }
    })

    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    return "other sent"

def send_nonbuttons(recipient_id, response):
    message_text = str(response)
    params = {
           "access_token": os.environ["ACCESS_TOKEN"]
    }

    headers = {
            "Content-Type": "application/json"
    }

    data = json.dumps({
               "recipient": {
                      "id": recipient_id
               },
               "message": {
                    "text": message_text,
                    "quick_replies":[{
                            "content_type":"text",
                            "title":"Breakfast",
                            "payload":"Breakfast"
                            },
                            {
                            "content_type":"text",
                            "title":"Lunch",
                            "payload":"Lunch"
                            },
                            {
                            "content_type":"text",
                            "title":"Dinner",
                            "payload":"Dinner"
                            },
                            {
                            "content_type":"text",
                            "title":"Dino",
                            "payload":"Dino"
                            }]
               }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


def send_gif_message(recipient_id, message):
    gif_url = search_gif(message)

    data = json.dumps({
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": gif_url
                }
            }}
    })

    params = {
        "access_token": os.environ["ACCESS_TOKEN"]
    }

    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                      params=params, headers=headers, data=data)


if __name__ == "__main__":
    app.run()


def search_gif(text):
    #get a GIF that is similar to text sent
    payload = {'s': text, 'api_key': 'ey1oVnN1NGrtEDHFGBJjRj5AgegLFVeT', 'weirdness': 1}
    r = requests.get('http://api.giphy.com/v1/gifs/translate', params=payload)
    r = r.json()
    # sprint(r)
    try:
        url = r['data']['images']['original']['url']
    except:
        print('failed to get gif')

    return url



