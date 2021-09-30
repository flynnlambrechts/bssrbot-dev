# BssrBot 3.5.1
> Basser's Dino Menu, Shop and Calendar Assistant

## Requirements

Wit.ai - Language process (no longer used)
Heroku - Hosting code
NewRelic https://elements.heroku.com/addons/newrelic - Prevents code from idling
Database: postgresql - stores information input by users

## To Do
- Dino - done
- Shopen - done
- Add shop catalogue -done
- Calendar - done
- Wildcat of the week nominations
- Ressies
- BssrBot v4


## To Update menu
1. Name menu "menu.pdf" and place and in menu folder (remove old menu items)
2. Run camelot.py to generate menu htmls
3. In the thescrape2 find what week of the year corresponds to current menu week and update subtract value
4. (Optional) Reduce multiples of 4 in thescrape2 to only possible values

## To Update calendar
1. \copy data into db using heroku:
	\copy calendar FROM <path_to_calednar.csv> WITH (FORMAT CSV);
2. Go to calendar1 and zero week in getaway function
3. Push changes
### Formatting Calendar
- Make sure have a zero row at top with days in
- change nulls to blanks and then update line in calendar1

## Capabilities
- Return meal from Dino, breakfast, lunch and dinner
 	- including tomorrow and days of week
- Crack a joke
- Greetings
- Process pleasantries
- Get user's name
- Shopen
- Easter Eggs
- Shop catalogue
- Dinotimes
- Dino Feedback link
- Calendar
	- Week by week
	- Days
	- Week numbers
	- next week
- So much more

## Work On
- clean up shopen

## BssrBot v4 Coming Features
### Coffee Night
- Wildcat of the week Nominations
- Quote of the week submission
- Photo submissions (for slide show)
- Coffee Night Notificaitons? (Opt in and opt out)
### Usability
- Set week of term easier (admin)
- Set week of dino easier (admin)
- Register users college

Github# bssrbot-dev
