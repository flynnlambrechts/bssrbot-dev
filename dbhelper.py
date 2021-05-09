import sqlite3
import time
import datetime

openness = 1

conn = sqlite3.connect('bssrbot.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

#manually enter data
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(180902,'2021-08-11 13:53:39','Shopen',1)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = openness

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()

create_table() #only run once

for i in range(2):
    dynamic_data_entry()
    time.sleep(1)
#data_entry()


c.close()
conn.close()
