from flask import Flask
from flask import render_template

app = Flask(__name__)

import db_model as db
import json

from datetime import date
from datetime import timedelta

@app.route("/")
def index():

    results = db.select_one()
    print(results)
    return render_template("index.html")

@app.route("/hello")
def hello():

    results = db.select_one()
    return render_template("hello.html")



if __name__ == "__main__":
    app.run('0.0.0.0')
