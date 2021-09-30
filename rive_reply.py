##rive reply
## RIVESCRIPT STUFF MOVE FUNCTIONS INTO SEPERATE FILE
import datetime

from bot_constants import TIMEZONE
from rivescript import RiveScript
from bot_functions import PrintException
from models import (Sender, GlobalVar)
from response import (Response, UrlButton, QuickReply, Gif, Image)
from coffee_night import (add_nomination, add_quote)

bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

def set_vacuum(rs, location):
    try:
        psid = bot.current_user()
        location = " ".join(location)
        person = Sender(psid).get_fullname()
        time_now = datetime.datetime.now(TIMEZONE)
        print(time_now)
        GlobalVar('vacuum').update({'index':1,'location':location,'person':person,'time':time_now})
        return "Hope you had a good 'cuum. The location has been updated"
    except:
        PrintException()
    
def get_vacuum(rs, args):
    row = GlobalVar('vacuum').get()
    location = row[1]
    person = row[2]
    time = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S.%f%z')
    time = time.strftime('%I:%M%p, %d %b')
    return f"Vacuum Logs: \nLast Used by: {person} \nTime: {time} \nLocation left: {location}"


# Vacuum Functions
bot.set_subroutine("set_vacuum", set_vacuum)
bot.set_subroutine("get_vacuum", get_vacuum)
# bot.set_subroutine("greetings", greetings)

# Coffee Night Functions
bot.set_subroutine("add_nomination", add_nomination)
bot.set_subroutine("add_quote", add_quote)
#bot.set_subroutine("add_quote", add_quote)

def rive_response(recipient_id, message):
	response = bot.reply(str(recipient_id), message)
	return response