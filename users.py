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
        cur.execute('''CREATE TABLE users (
            full_name VARCHAR(100) PRIMARY KEY NOT NUll,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            PSID INTEGER NOT NULL
            )''')
        print("User Table created successfully")
        con.commit()
    except Exception as error:
        response = response + "Fail in adding users table: " + str(error)
        print("Error: " + str(error) + "\n" + str(type(error)))
    return response

def insert_user(full_name, first_name, last_name, PSID):
    global con
    response = ""
    try:
        cur = con.cursor()
        cur.execute('''INSERT INTO users (
            full_name,
            first_name,
            last_name,
            PSID)
            VALUES (%s,%s,%s,%s)''',
                    (full_name, first_name, last_name, PSID))
        print("User data inserted successfully")
    except Exception as error:
        #response = response + "Fail in insert user: " + str(error)
        print("Error: " + str(error) + "\n" + str(type(error)))

#create_users()
#con.close()
