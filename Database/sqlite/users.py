from sys import argv as argument
try:
    argument[1]
except IndexError:
    exit()

import sqlite3


connection = sqlite3.connect('users.db')
c = connection.cursor()

if argument[1] == "insert":
    user_name = input("Name: ")
    user_age = input("Age: ")
    c.execute("INSERT INTO users VALUES (?, ?)", (user_name, user_age))

elif argument[1] == "show":
    username = input("User-Name: ")
    c.execute("SELECT * FROM users WHERE name=?", (username,))
    print(c.fetchone())

connection.commit()
connection.close()
