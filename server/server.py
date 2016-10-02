from flask import Flask, request
from flask import render_template

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/")
def index():
	#using a user_id 0
   	db.add_goal('sleep', 0, 'hours', 8)
   	goals = db.select_goals(0)

   	return render_template("index.html", goals=goals)

@app.route("/signup")
def signup():
    return render_template("signup.html")

    #results = db.select_one()

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
   	result = request.form
   	return render_template("result.html",result = result)



if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')

#
