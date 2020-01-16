# Three Stooges -- Saad Bhuiyan (PM), Benjamin Avrahami, Hannah Fried
# SoftDev1 pd2
# P02 -- The End
# 2020-01-07

import os
import random
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from urllib.request import urlopen
from utl import db
import json


# create instance of class Flask
app = Flask(__name__)


# set up sessions with random secret key
app.secret_key = os.urandom(32)     # for deployment
# app.secret_key = "Stooges"        # for debugging


print("checking for LocationIQ api key in api_key.txt...")
with open("api_key.txt", "r+") as api_key:
    global locationiq_api_key
    if api_key.readline() == "":
        print("looks like you haven't entered your LocationIQ api key")
        print("please follow the instructions in README.md to get a key")
        locationiq_api_key = input("then enter your api key here: ")
        print("saving LocationIQ api key in api_key.txt...")
        api_key.write(locationiq_api_key)
        print("api key saved, you are good to go!")
        api_key.close()
    else:
        print("api key found")
        locationiq_api_key = api_key.readline()


# db.init(locationiq_api_key)

try:
    db.init()
except:
    print("database has already been initialized and populated")


#=====DECORATOR=FUNCTIONS===================================================
# Decorator functions to eliminate redundancy:

# Login checking
def protected(route_function):
    def login_check(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for("login"))
        return route_function(*args, **kwargs)
    login_check.__name__ = route_function.__name__
    return login_check

#============================================================================


# root redirects to login if the user isn't logged in, and home if they are
@app.route("/")
def root():
    # if user is logged in, redirect to home
    if "username" in session:
        return redirect(url_for("home"))
    # else redirect to login
    return redirect(url_for("login"))


# login page and authentication of login
@app.route("/login")
def login():
    # if user is logged in, redirect to home
    if "username" in session:
        return redirect(url_for("home"))
    # if users attempts login
    if len(request.args) >= 2:
        # if inputted login info is correct, adds user to session and redirects to home
        if db.authenticate_user(request.args["username"], request.args["password"]):
            session["username"] = request.args["username"]
            return redirect(url_for("home"))
        # else flashes error message and redirects back to login
        else:
            flash("Incorrect username or password, please check spelling and captilization.")
    # render login template
    return render_template("login.html")


# register page and validation
@app.route("/register")
def register():
    # if user is logged in, redirect to home
    if "username" in session:
        return redirect(url_for("home"))
    # if user attempts registration
    if len(request.args) >= 3:
        # if any one of the three fields are blank, flash error
        if request.args["username"] == "" or request.args["password1"] == "" or request.args["password2"] == "":
            flash("Please do not leave any fields blank.")
        # if the passwords don't match, flash error
        elif request.args["password1"] != request.args["password2"]:
            flash("Passwords don't match.")
        # else if adding the user (to the database) is successful, username must be unique
        elif db.add_user(request.args["username"], request.args["password1"]):
            # if the username is unique, session is added and user is redirected to home
            session["username"] = request.args["username"]
            return redirect(url_for("home"))
        # else flash error
        else:
            flash("Username not unique.")
    # render register template
    return render_template('register.html')


# logout will pop username from the session and redirect to login
@app.route("/logout")
@protected
def logout():
    # if user is logged in
    if "username" in session:
        # pop "username" from session
        session.pop("username")
    # redirect user back to login page
    return redirect(url_for("login"))


# information about the project - what? how? etc.
@app.route("/home")
@protected
def home():
    nations_data=list()
    all_nations=db.return_nations()
    for nation in all_nations: # nation data to pass to template
        nations_data.append(db.data(nation))
    faves = db.get_favorites(session["username"]) # grab favorites for user
    if faves != None: # if there are favorites
      faves = faves.split(",") # split into list
    else:
      faves = []
    return render_template("home.html",
                            nations=nations_data,
                            favorites=faves)


@app.route("/settings", methods=['GET','POST'])
@protected
def settings():
    username = session["username"]
    if len(request.args) >= 3:
        # if any one of the three fields are blank, flash error
        if request.args["oldpassword"] == "" or request.args["newpassword1"] == "" or request.args["newpassword2"] == "":
            flash("Please do not leave any fields blank.")
        # if the new passwords don't match, flash error
        elif request.args["newpassword1"] != request.args["newpassword2"]:
            flash("Passwords don't match.")
        # else update password
        elif db.update_password(username, request.args["oldpassword"], request.args["newpassword1"]):
            flash("Password updated.")
        # else if false is returned by db
        else:
            flash("Password incorrect.")
    return render_template("settings.html")


@app.route("/browse")
@protected
def browse():
    nations_data=list()
    all_nations=db.return_nations()
    for nation in all_nations: # nation data to pass to template
        nations_data.append(db.data(nation))
    faves = db.get_favorites(session["username"]) # grab favorites for user
    if faves != None: # if there are favorites
      faves = faves.split(",") # split into list
    else:
      faves = []
    return render_template("browse.html",
                            nations=nations_data,
                            favorites=faves)

@app.route("/fav")
@protected
def refavorite():
    print(request.args["nation"])
    if request.args["submit"] == "Favorite this Nation": # if user clicks favorite on card
        db.add_favorite(session["username"],request.args["nation"]) # add to favorite
    else: # if user clicks unfavorite
        db.remove_favorite(session["username"],request.args["nation"]) # remove from favorites
    return redirect(url_for("home"))


@app.route("/nation/<nation_code>")
@protected
def nation(nation_code):
    nat = db.return_nations()
    facts = dict()
    for i in nat: # data for nation
        if i.replace(" ","") == nation_code:
            facts = db.data(i)
    # get woeid for the capital from metaweather
    metaweather_woeid = "https://www.metaweather.com/api/location/search/?lattlong=" + facts["capitallat"] + "," + facts["capitallon"]
    woeid = json.loads(urlopen(metaweather_woeid).read())
    woeid = str(woeid[0]["woeid"])
    # call metaweather api with woeid
    metaweather_api_call = "https://www.metaweather.com/api/location/" + woeid
    metaweather_data = json.loads(urlopen(metaweather_api_call).read())
    # weather data to pass to template
    weather0 = metaweather_data["consolidated_weather"][0]
    weather1 = metaweather_data["consolidated_weather"][1]
    weather2 = metaweather_data["consolidated_weather"][2]
    weather3 = metaweather_data["consolidated_weather"][3]
    weather4 = metaweather_data["consolidated_weather"][4]
    return render_template("nation.html",
                            nation=facts["nation"],capital=facts["capital"],flag=facts["flag"],
                            area=facts["area"],population=facts["population"],
                            lat=facts["nationlat"], lon=facts["nationlon"],
                            clat=facts["capitallat"], clon=facts["capitallon"],
                            zoom=facts["zoom"],
                            weather0=weather0,weather1=weather1,weather2=weather2,weather3=weather3,weather4=weather4)


#============================================================================


if __name__ == "__main__":
    # app.debug = True
    app.debug = False
    app.run()
