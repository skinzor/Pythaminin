import sqlite3
from sys import argv as argument
from os import remove

try:
    if argument[1] == "flush":
        confirmation = input("Are you sure? y/n ")
        if confirmation.lower() == "y":
            remove("users.db")
        else:
            db_file = input("Enter File name to remove: ")
            remove(db_file)
except IndexError:
    pass

connection = sqlite3.connect("users.db")
c = connection.cursor()

c.execute("""CREATE TABLE users (
            name text,
            age integer
            )""")

connection.commit()
connection.close()
