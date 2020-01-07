# Three Stooges -- Saad Bhuiyan (PM), Benjamin Avrahami, Hannah Fried
# SoftDev1 pd2  
# P02 -- The End
# 2020-01-07


# DATABASE INTERACTIONS


# importing the sqlite3 module to interface with sqlite databases
import sqlite3


_DB_FILE = 'stooges.db'


# connects to the database file
# passes the connected object to the wrapped function
# returns the wrapped function if no SQLite error, otherwise False
def _connects(db_func):
    def establish_connection(*args, **kwargs):
        db = sqlite3.connect(_DB_FILE)
        try:
            return db_func(*args, **kwargs, db = db)
        except sqlite3.Error as error:
            print(error)
            return False
    return establish_connection


# creates tables in the database
@_connects
def init(db=None):
    # initializing the users table
    # stores user login data
    db.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER UNIQUE PRIMARY KEY, 
                    username TEXT UNIQUE, 
                    password TEXT
                );
               ''')
    db.commit()