# Three Stooges -- Saad Bhuiyan (PM), Benjamin Avrahami, Hannah Fried
# SoftDev1 pd2
# P02 -- The End
# 2020-01-07


# DATABASE INTERACTIONS


# importing the sqlite3 module to interface with sqlite databases
import sqlite3
import csv       # facilitate CSV I/O
from urllib.request import urlopen
import json
import time


DB_FILE = 'stooges.db'

locationiq_api_key = "af54e0b0e10a5c"


# initializes the database tables if they don't exist
def init():
    print("initializing database...")
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    # creating the users table
    c.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER UNIQUE PRIMARY KEY, username TEXT UNIQUE, password TEXT, favorites TEXT);") # iptracking TEXT DEFAULT 'False', removed
    c.execute("CREATE TABLE IF NOT EXISTS nations(nation_id INTEGER UNIQUE PRIMARY KEY, nation TEXT UNIQUE, code TEXT UNIQUE, rating TEXT, image TEXT, capital TEXT, population INTEGER, area INTEGER, nationlat TEXT, nationlon TEXT, capitallat TEXT, capitallon TEXT, zoom TEXT);")
    db.commit() # save changes
    db.close() # close database
    print("database initialized")
    populate_database()


# populate database with information necessary for demo as well as nation data
def populate_database():
    print("populating database...")
    print("create admin: " + str(add_user("admin", "password")))
    print("cache data from REST Countries API...")
    fill_nations()
    print("data cached")
    print("add favorite nation United States of America to admin: " + str(add_favorite("admin", "United States of America")))
    print("add favorite nation Switzerland to admin: " + str(add_favorite("admin", "Switzerland")))
    print("database populated")


# fill nations table with data
def fill_nations():
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    with open("nations.csv") as file: # nnations.csv opened
        file = csv.DictReader(file) #read through file using DictReader
        for row in file: # goes through each row of the file
            print("updating " + row["nation"] + " in database from csv and api")
            restcountries_api_call = "https://restcountries.eu/rest/v2/alpha/" + row["code"]
            restcountries_data = json.loads(urlopen(restcountries_api_call).read())
            nation_name = row["nation"].replace(" ", "%20")
            locationiq_nation_api_call = "https://us1.locationiq.com/v1/search.php?&q=" + nation_name + "&format=json&key=" + locationiq_api_key
            locationiq_nation_data = json.loads(urlopen(locationiq_nation_api_call).read())
            time.sleep(1)
            capital_name = restcountries_data["capital"].replace(" ", "%20")
            if row["code"] == "US":
                capital_name = "Washington"
            if row["code"] == "BR":
                capital_name = "Brasilia"
            if row["code"] == "CO":
                capital_name = "Bogota"
            locationiq_capital_api_call = "https://us1.locationiq.com/v1/search.php?&q=" + capital_name + "&format=json&key=" + locationiq_api_key
            locationiq_capital_data = json.loads(urlopen(locationiq_capital_api_call).read())
            time.sleep(1)
            c.execute("INSERT INTO nations(nation,code,rating,image,capital,population,area,nationlat,nationlon,capitallat,capitallon,zoom) VALUES(?,?,?,?,?,?,?,?,?,?,?,?);", 
                            (row["nation"],row["code"],row["rating"],row["image"],
                            restcountries_data["capital"],restcountries_data["population"],restcountries_data["area"],
                            locationiq_nation_data[0]["lat"],locationiq_nation_data[0]["lon"],locationiq_capital_data[0]["lat"],locationiq_capital_data[0]["lon"],row["zoom"]))
    db.commit() # save changes
    db.close() # close database


# function to register a user if the username doesn't exist in the database
def add_user(username, password):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    status = True
    c.execute("SELECT * FROM users WHERE username = ?;" , (username,)) # query rows where the username and input username match
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


# function to update a user's password
def update_password(username, oldpassword, newpassword):
    if not authenticate_user(username, oldpassword): # if the user's old password is incorrect
        return False # password will not be updated
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    c.execute("UPDATE users SET password = ? WHERE username = ?;" , (newpassword, username)) # update password for a user
    db.commit() # save changes
    db.close() # close database
    return True


# function to get a user's favorites
def get_favorites(username):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    c.execute("SELECT favorites FROM users WHERE username = ?;" , (username,)) # query favorites where username matches
    for row in c.fetchall(): # rows that are queried
        favorites = row[0] # set favorites to queried row
    db.commit() # save changes
    db.close() # close database
    return favorites


# function to add a favorite nation to a user's favorites
def add_favorite(username, nation):
    favorites = get_favorites(username) # get favorites using helper function
    if favorites == None: # if there are no favorites
        favorites = nation + "," # favorites is just the nation with a comma
    else: # if there is a list of favorites
        if nation in favorites: # if the nation is in that list
            return False
        favorites = favorites + nation + "," # otherwise, add the nation to that list
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    c.execute("UPDATE users SET favorites = ? WHERE username = ?;" , (favorites, username)) # update favorites with new list
    db.commit() # save changes
    db.close() # close database
    return True


# function to remove a nation from a user's favorites
def remove_favorite(username, nation):
    favorites = get_favorites(username) # get favorites using helper function
    if favorites == None: # if there are no favorites
        return False
    if nation not in favorites: # if the nation is in the list of favorites
        return False
    favorites = favorites.replace(nation + ",", "")
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    c.execute("UPDATE users SET favorites = ? WHERE username = ?;" , (favorites, username)) # update favorites with new list
    db.commit() # save changes
    db.close() # close database
    return True


# function to return the all nations' names
def return_nations():
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    all_names = list()
    c.execute("SELECT nation FROM nations ORDER BY nation;") # query all nation names ordered alphabetically
    for row in c.fetchall():
        all_names.append(row[0])
    db.commit() # save changes
    db.close() # close database
    return all_names


# function to return the rating of a nation
def data(nation):
    db = sqlite3.connect(DB_FILE) # open file
    c = db.cursor() # facilitate db ops
    c.execute("SELECT * FROM nations WHERE nation = ?;" , (nation,))
    data = dict()
    for row in c.fetchall(): # rows that are queried
        data["nation_id"] = row[0]
        data["nation"] = row[1]
        data["code"] = row[2]
        data["rating"] = row[3]
        data["image"] = row[4]
        data["capital"] = row[5]
        data["population"] = row[6]
        data["area"] = row[7]
        data["nationlat"] = row[8]
        data["nationlon"] = row[9]
        data["capitallat"] = row[10]
        data["capitallon"] = row[11]
        data["zoom"] = row[12]
    db.commit() # save changes
    db.close() # close database
    return data


# function to return api call for map of a nation
def map(nation):
    info = data(nation)
    key = "key=" + locationiq_api_key
    center = "&center=" + info["nationlat"] + "," + info["nationlon"]
    zoom = "&zoom=" + info["zoom"]
    size = "&size=" + "700x400"
    marker = "&markers=icon:small-purple-cutout|" + info["capitallat"] + "," + info["capitallon"]
    api_call = "https://maps.locationiq.com/v2/staticmap?" + key + center + zoom + size + marker
    return api_call