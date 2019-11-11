#! /usr/bin/python3

import sqlite3

con = sqlite3.connect('/home/pi/django_school/db.sqlite3')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    #cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursorObj.execute("SELECT * FROM auth_group")
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)
 
sql_fetch(con)
