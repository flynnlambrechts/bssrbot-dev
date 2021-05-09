import os
import psycopg2

import time
import datetime


ENV = "HEROKU"
if ENV == "LOCAL":
    con = psycopg2.connect(database="bssrbot1", user="flynnlambrechts", password="", host="127.0.0.1", port="5432")
    print("Local Database opened successfully")
if ENV == "HEROKU":
    DATABASE_URL =  os.environ['DATABASE_URL']
    con = psycopg2.connect(DATABASE_URL, sslmode='require')
else:
    print("ENV specified wrong.")
    

global person
person = str("Wendy")

global current_time, end_time, date
unix = int(time.time())
current_time = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))
date_and_time = datetime.datetime.fromtimestamp(unix)
end_time = date_and_time + datetime.timedelta(hours=3) #closes shop after 3 hours
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))


def create_shopen():
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
    #con.close()
    return response


def open_shopen():
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
    cur = con.cursor()
    cur.execute('''SELECT * FROM shopen''')
    rows = cur.fetchall()
    response = ""
    for row in rows:
        print("person =", row[0])
        response = response  + "Person = " + str(row[0])
        print("start_time =", row[1])
        response = response  + " start_time = " + str(row[1])
        print("end_time =", row[2])
        response = response + " end_time = " + str(row[2])
        print("value =", row[3])
        response = response + " value = " + str(row[3])
        print("date =", row[4], "\n")
    return response
        



