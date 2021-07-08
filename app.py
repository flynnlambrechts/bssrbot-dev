  
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
            if message.get('message'):
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    message_text = message['message']['text']
                    print(message_text)
                    get_bot_response(recipient_id,message_text)
                elif message['message'].get('attachments'):
                    print("Picture")
                    attachment = "blank for now"
                    get_bot_response(recipient_id, attachment)
                else:
                    print("No message?")
                    log(output)


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
    


if __name__ == "__main__":
    app.run()




