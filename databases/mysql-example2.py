#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="lala",  # your password
                     db="sqlexamples")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT b1 FROM b")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()
