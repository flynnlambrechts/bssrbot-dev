#TheScrape3
from datetime import *
import time

from pytz import timezone

from getmenuweek import getmenuweek
from getmenuweek import checkForDay
from killswitch import read_custom_message
from bot_constants import week_days


TIMEZONE = timezone('Australia/Sydney')


class Meal:
	def __init__(self, meal=None, day=None, week=None):
		self.week = getmenuweek() #week defaults to current week of cycle
		self.menu = ""
		self.Range = 0
		self.page = 0

	def setday(self):

	def setweek(self):

	def getmenu(self ,current_day, column, week):
	    for i in range(0,self.Range):
	        try:
	            header = ""
	            column = 0
	            header = header + columnlist(page, column, Range)[i]
	            header = addemojis(header)
	            content = ""
	            if current_day == 7: #if its after sunday
	                column = 1 #it must be monday
	            else:
	                column = current_day + 1
	            content = content + columnlist(self.page, column, self.Range)[i]
	            if content != "":
	                content = addemojiscontent(content)
	                self.menu = "".join([self.menu,str(header).title(),": \n",str(content).capitalize(),"\n\n"])
	        except IndexError:
	            print('NOK')
	    return self.menu

	def getresponse(self):
		response = f"{meal} {day}: \n"

class Breakfast(Meal):
	def __init__(self, meal=None, day=None, week=None):
		self.Range = 3
		self.page = str((2*(week-1)+1))
		self.menu = ""

class Lunch(Meal):
	def __init__(self, meal=None, day=None, week=None):
		self.Range = 2
		self.page = str((2*(week-1)+1.5))
		self.menu = ""

class Dinner(Meal):
	def __init__(self, meal=None, day=None, week=None):
		self.Range = 8
		self.page = str((2*(week-1)+2))
		self.menu = ""


def getDino(message, con, value):

	time = datetime.now(TIMEZONE).time().hour

	day, current_day, column, week = getDay(message, week)

	if value == "dino":
		if day == "Tomorrow":
			meal = Breakfast()
		elif time < 10:
			meal  = Breakfast()
        elif time < 14:
            meal = Lunch()
        elif time < 19:
            meal = Dinner()
        else: 
            day = "Tomorrow"
            current_day += 1
            meal = Breakfast()

    elif value == "breakfast":
    	if time > 14 and day == "Today": #after 2pm will give the breakfast for the next day
    		day = "Tomorrow"
    		#UP TO HERE

def getmenuweek():
    x = datetime.datetime.now(TIMEZONE)
    week = (int(x.strftime("%W"))+1) #plus one changes the cycle to match the dino cycle
    menuweek = (week)%4+1 #this cheeky +1 changes range from (0-3 to 1-4)
    print(menuweek)
    return menuweek

def getDay(message, week): #here is where we get the day and current_day and sometimes week
    column = ""

    current_day = datetime.now(TIMEZONE).weekday()
    day = "Today"
    
    #See if user is asking about tomorrow
    if "tomorrow" in message or "tmrw" in message or "tomoz" in message or "tmoz" in message:
        day = "Tomorrow"
        current_day+=1
        time = 0
        if current_day==7:
            if week==4:
                week = 1
                print(str(week) + " week")
                column = 1
            else:
                week = week + 1
                print(str(week) + "week")
                column = 1

    #check if user has asked about a day of the week
    elif checkForDay(message):
        print("Day Found!")
        daynumber = int(checkForDay(message))
        if current_day > daynumber:
            print(str(week) + " week, checkForDay")
            if str(week)==str("4"):
                week = 1
                print(str(week) + " week, checkForDay if 4")
            else:
                week = week + 1
                print(str(week) + " week, checkForDay else")
            current_day = daynumber
            day = str(week_days[current_day])
        else:
            current_day = daynumber
            day = str(week_days[current_day])
    #otherwise must be today: and day and current_day are not updated from todays value
    return day, current_day, column, week

def checkForDay(message): #check of day of week specified
    day = ""
    if "monday" in message or " mon" in message or "mon " in message:
        day = str('0')
    elif "tuesday" in message or " tues" in message or "tues " in message:
        day = 1
    elif "wednesday" in message or " wed" in message or "wed " in message:
        day = 2 
    elif "thursday" in message or " thur" in message or "thur " in message or " thurs" in message or "thurs " in message:
        day = 3
    elif "friday" in message or " fri" in message or "fri " in message:
        day = 4
    elif "saturday" in message or " sat" in message or "sat " in message:
        day = 5
    elif "sunday" in message or " sun" in message or "sun " in message:
        day = 6
    return day

#GLOSSARY:
#current_day: day of week 0-6 inclusive
#daynumber:  day of week 0-6 inclusive represents day user asked for
#day_value: day of week 1-7 inclusive
#day: name of the day e.g. monday, wednesday, tomorrow, today
#week: week of cycle (1-4)
	
def addemojis(header):
    header = header.replace("salad", u"salad \U0001F957")
    if "vegetarian option" in header:
        header = header.replace("vegetarian option", u"vegetarian option \U0001F331")
    else:
        header = header.replace("vegetarian", u"vegetarian \U0001F331")
    header = header.replace("main course", u"main course \U0001F37D").replace("hot option", u"hot option \U0001F37D")
    header = header.replace("residential breakfast", u"residential breakfast \U0001f95e")
    header = header.replace("soup", u"soup \U0001f372")
    header = header.replace("the dessert station", u"the dessert station \U0001f370")
    header = header.replace("additional vegetables", u"additional vegetables \U0001F966")
    return header

def addemojiscontent(content):
    #content = content.replace("egg", u"egg \U0001F95A")
    content = content.replace("pancakes", u"pancakes \U0001f95e")
    content = content.replace("pizza", u"pizza \U0001f355")
    content = content.replace("sushi", u"sushi \U0001f363")
    content = content.replace("chicken", u"chicken \U0001F357")
    content = content.replace("honey", u"honey \U0001F36F")
    return content


def columnlist(page, column, Range): #gets the info from each column as a list
    rowcontents = []
    for i in range(0,Range):
        row = i
        content = getinfo(page, row, column)
        rowcontents.append(content)
    return rowcontents

def addnote(con, value, day):
    meal = value
    if day == "Today": #makes sure we are talking about the actual day e.g. not tommorrow or the coming wednesday
        try: 
            note = "".join(["Note:\n",read_custom_message(meal, con).capitalize()])
        except AttributeError:
            note = None
    else: #otherwise there is no note
        note = None 

    return note


def getinfo(page, row, column): #this is where the scraping happens
    #-----------------------Opening the HTML file--------------------------#
    HTMLFile = open(str("menu/" + page + ".html"), "r") #try putting in func.
    #print(str(HTMLFile))
    # Reading the file
    index = HTMLFile.read()
      
    # Creating a BeautifulSoup object and specifying the parser
    soup = BeautifulSoup(index, 'lxml')

    # Using the prettify method to modify the code
    #print(soup.body.prettify())

    #print(soup.title) #prints the table title if it has one

    menu_table = soup.find("table", attrs={"class": "dataframe"})
    menu_table_data = menu_table.tbody.find_all("tr")  # contains 2 rows

    #---------------------------------------------------------------------#
    info = []
    for td in menu_table_data[row].find_all("td"):
        if td is not None:
            #plain_text = str(td).replace(r"– \n \n","- ").replace(r" \n \n", ", ").replace(r"– \n", "- ").replace(r"\n–","-").replace(", \n",", ").replace(r" \n ","").replace(r" \n",", ").replace(r"\n",", ")
            stuff = str(td).replace("<td>","").replace("</td>","").replace("amp;","").replace(r"\n","")
            #plain_text  =  stuff.strip(""",.;:-¢"'�_!?I•,L4J£<~""") #removes all weird artifacts
            info.append(stuff)
        else:
            print("none!")
    return info[column]



