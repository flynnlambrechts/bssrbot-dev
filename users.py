#users
import psycopg2

from connectdb import connectToDB
from connectdb import con
global con

connectToDB()

def create_users():
    global con
    cur = con.cursor()
    response = ""
    try:
        cur.execute('''CREATE TABLE ressies (
            first_name VARCHAR(50) PRIMARY KEY NOT NULL,
            last_name VARCHAR(50) PRIMARY KEY NOT NULL,
            PSID INTEGER NOT NULL
            )''')
        print("Table created successfully")
        con.commit()
    except Exception as error:
        response = response + "Fail: " + str(error)
        print("Error: " + str(error) + "\n" + str(type(error)))
    return response

def insert_user(first_name, last_name, PSID):
    global con
    try:
        cur = con.cursor()
        cur.execute('''INSERT INTO ressies (
            first_name,
            last_name,
            room_number)
            VALUES (%s,%s,%s)''',
                    (first_name, last_name, PSID))
        print("User data inserted successfully")
    except Exception as error:
        response = response + "Fail: " + str(error)
        print("Error: " + str(error) + "\n" + str(type(error)))

create_users()
