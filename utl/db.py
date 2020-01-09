# Three Stooges -- Saad Bhuiyan (PM), Benjamin Avrahami, Hannah Fried
# SoftDev1 pd2  
# P02 -- The End
# 2020-01-07


# DATABASE INTERACTIONS


# importing the sqlite3 module to interface with sqlite databases
import sqlite3


DB_FILE = 'stooges.db'


# initializes the database tables if they don't exist
def init():
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    # creating the users table
    c.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER UNIQUE PRIMARY KEY, username TEXT UNIQUE, password TEXT, iptracking TEXT DEFAULT 'False');")
    db.commit() # save changes
    db.close() # close database


# function to register a user if the username doesn't exist in the database
def add_user(username, password):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    status = True                  
    c.execute("SELECT * FROM users WHERE username = ?;" , (username)) # query rows where the username and input username match
    if c.fetchone() is None: # if the username does not already exist in the database
        c.execute("INSERT INTO users(username, password) VALUES(?, ?);" , (username, password)) # stores the input login credentials in the users table
    else:
        status = False # user is not added when the username is found in the users table
    db.commit() # save changes
    db.close() # close database
    return status


# function to authenticate whether a user exists and the password is correct
def authenticate_user(username, password):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    status = True
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?;" , (username, password)) # query rows where the input name and password match
    if c.fetchone() is None: # if login credentials are not found in the users table
        status = False
    db.commit() # save changes
    db.close() # close database
    return status


# function to retrieve a user's iptracking setting
def check_iptracking(username):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    setting = False
    c.execute("SELECT iptracking FROM users WHERE username = ?;" , (username)) # query rows where the input name and password match
    for row in c.fetchall(): # rows that are queried
        if (row[0] == "True"): # if iptracking is true
            setting = True # setting is changed to true
    db.commit() # save changes
    db.close() # close database
    return setting

# function to set a user's iptracking setting
def set_iptracking(username, setting):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    c.execute("UPDATE users SET iptracking = ? WHERE username = ?;" , (setting, username)) # update ip tracking setting for a user
    db.commit() # save changes
    db.close() # close database
    return setting