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

    # results = db.select_one()
    # print(results)
    return render_template("index.html")

@app.route("/signup")
def signup():

    return render_template("signup.html")

@app.route("/member")
def member():

    return render_template("member.html")

if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')

#
