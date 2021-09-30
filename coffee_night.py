#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos
import datetime
from bot_constants import TIMEZONE

from models import Sender



#--- Photo Submission




# def set_vacuum(rs, location):
#     try:
#         psid = bot.current_user()
#         location = " ".join(location)
#         person = Sender(psid).get_fullname()
#         time_now = datetime.datetime.now(TIMEZONE)
#         print(time_now)
#         GlobalVar('vacuum').update({'index':1,'location':location,'person':person,'time':time_now})
#         return "Hope you had a good 'cuum. The location has been updated"
#     except:
#         PrintException()
#     