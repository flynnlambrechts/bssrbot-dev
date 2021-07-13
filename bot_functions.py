#Bot Functions
import os, sys
import psycopg2
from linecache import (checkcache, getline) # for error handling
from bot_constants import DATABASE_URL

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    checkcache(filename)
    line = getline(filename, lineno, f.f_globals)
    print(f'EXCEPTION IN ({filename}, LINE {lineno} "{line.strip()}"): {exc_obj}')

def getCon(): #gets the connection  to the database when required
    if "HEROKU" in os.environ:
        DATABASE_URL =  os.environ['DATABASE_URL']
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
    else:
        con = psycopg2.connect(database="bssrbot1", user="flynnlambrechts", password="", host="127.0.0.1", port="5432")
        print("Local Database opened successfully")
    return con

# Vacuum functions
def set_vacuum(rs, location):
    get_bot_response.bot.set_variable('vacuum', location)
    if location:
        get_bot_response.bot.set_variable('vacuum', location)
        return "Hope you had a good 'cuum. The location has been updated"

def get_hashbrowns(rs, args):
    if get_bot_response.bot.get_variable('vacuum'):
        vacuum = get_bot_response.bot.get_variable('vacuum')
        return f"Vacuum was last left {vacuum}. Happy 'cuuming."
    else:
        return "Oh no, it seems i've got no idea where the 'cuum is. :("