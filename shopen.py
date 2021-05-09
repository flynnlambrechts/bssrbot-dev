import os
import psycopg2

import time
import datetime
import pytz

TIMEZONE = pytz.timezone('Australia/Sydney')

from connectdb import connectToDB
from connectdb import con
global con   

global person
person = str("Wendy")

global current_time, end_time, date
current_time = datetime.datetime.now(TIMEZONE).strftime('%H:%M:%S')
date_and_time = datetime.datetime.now(TIMEZONE)
end_time = (date_and_time + datetime.timedelta(hours=3)).strftime('%H:%M:%S') #closes shop after 3 hours
date = str(datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d'))


def create_shopen():
    global con
    cur = con.cursor()
    response = ""
    try: 
        cur.execute('''CREATE TABLE shopen
            (person VARCHAR(50) NOT NULL PRIMARY KEY,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            value BOOLEAN NOT NULL,
            date DATE NOT NULL)
            ''')
        print("Table created successfully")
        response = response + "Table created."
        con.commit()
    except Exception as error:
        response = response + "Fail: " + str(type(error))
    return response

def insert_shopen():
    global con
    global person
    global current_time, end_time, date
    response = ""
    try:
        cur = con.cursor()
        cur.execute('''INSERT INTO shopen (
            person, start_time, end_time, value, date)
            VALUES (%s,%s,%s,%s,%s)''',
                (person,current_time,end_time,'true',date))
        print("Shopen data inserted successfully")
        response  = response + "Shop row inserted"
        con.commit()
    except Exception as error:
        response = response + "Fail: " + str(type(error))
    return response


def open_shopen():
    global con
    global person
    global current_time, end_time, date
    cur = con.cursor()
    cur.execute('''UPDATE shopen SET
        person= %s, start_time = %s, end_time = %s, value = %s,
        date = %s''',
            (person,current_time,end_time,'true',date))
    print("Shopen updated successfully")
    con.commit()
    return "Shop has been opened"

def close_shopen():
    global con
    global person
    unix = int(time.time())
    current_time = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))
    cur = con.cursor()
    cur.execute('''UPDATE shopen SET
        person= %s, end_time = %s, value = %s''',
            (person, current_time,'false'))
    print("Shopen updated successfully")
    con.commit()
    return "Shop has been closed"

def get_shopen():
    global con
    cur = con.cursor()
    cur.execute('''SELECT * FROM shopen''')
    rows = cur.fetchall()
    response = ""
    for row in rows:
        '''
        print("person =", row[0])
        print("start_time =", row[1])
        print("end_time =", row[2])
        print("value =", row[3])
        print("date =", row[4], "\n")
        '''
        person = row[0]
        start_time = row[1]
        end_time = row[2]
        value = row[3]
        date = row[4]
    if value == "True":
        response = response + "Yes shop was opened by " + person + " at " #+ start_time.strftime('%I:%M %p')
    elif value == "False":
        response = response + "Sorry, shop closed :("
    return response
        



