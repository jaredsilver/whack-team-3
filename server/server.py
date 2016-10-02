from flask import Flask, request
from flask import render_template

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
	return render_template("signup.html")

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
   	result = request.form
   	for key in result:
   		if key == "username":
   			username = key
   		if key == "password":
   			password = key
   	#create a user into the database with username and password 
   	return render_template("member.html",result = result)

@app.route("/member")
def member():
    return render_template("member.html")

if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')
