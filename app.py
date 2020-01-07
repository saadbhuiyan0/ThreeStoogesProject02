# Three Stooges -- Saad Bhuiyan (PM), Benjamin Avrahami, Hannah Fried
# SoftDev1 pd2  
# P02 -- The End
# 2020-01-07


import os
import random
from flask import Flask
from utl import db


# create instance of class Flask
app = Flask(__name__)

# set up sessions with random secret key
# app.secret_key = os.urandom(32)     # for deployment
app.secret_key = "Stooges"            # for debugging


# initialize database
db.init()