#Coffee Night Stuff
#Wildcat Nominations
#Quote Nominations
#Photos

from models import Sender

#--- Wildcat Nominations
def add_nomination(rs, args): 
# Recieves a list of words containing the persons name first followed by the reason
# E.g. ["Flynn", "for", "making", "BssrBot"]
	nominee = args[0]
	reason = " ".join(args[1:])

	psid = bot.current_user()
	person = Sender(psid).get_fullname()

	print(nomiee + " For " + reason + " By " + person)

#--- Quote Submission
def add_quote(rs, args):
	return args


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