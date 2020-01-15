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
# app.secret_key = os.urandom(32)     # for deployment
app.secret_key = "Stooges"            # for debugging


# db.init() 

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

#HTML_TEMPLATE = Template("""
#<h1>Hello ${some_place}!</h1>

#<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${some_place}" alt="map of ${some_place}">

#<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${some_place}" alt="street view of ${some_place}">
#""")

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
    faves = db.get_favorites(session["username"]).split(",")
    faves.pop(len(faves)-1)
    return render_template("home.html",
                            favorites = faves)

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
    for nation in all_nations:
        nations_data.append(db.data(nation))
    print(nations_data)
    return render_template("browse.html",
                            nations=nations_data)

@app.route("/country")
@protected
def testmap():
    return render_template("country.html")

@app.route("/nation")
@protected
def nation(nation):
    return(HTML_TEMPLATE.substitute(some_place=nation))


#============================================================================


if __name__ == "__main__":
    app.debug = True
    app.run()
