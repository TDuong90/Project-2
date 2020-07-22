import requests, json
from flask import Flask, render_template, redirect, jsonify
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# response = requests.get("https://data.lacity.org/resource/d5tf-ez2w.json").json()
# print(response[0].keys())

engine = create_engine("sqlite:///sqlite_traffic_weather.db")

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Traffic = Base.classes.traffic_data_clean_final
# Weather = Base.classes.national-weather-service

session = Session(engine)

app = Flask(__name__)


@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/home<br/>"
        f"/api/v1.0/dates<br/>"
        f"/api/v1.0/locations<br/>"
        f"/api/v1.0/addresses<br/>"
        f"/api/v1.0/victimsexes<br/>"
    )

@app.route("/api/v1.0/home")
def index():
    print("home")
    return render_template("index.html")


@app.route("/api/v1.0/dates")
def dates():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all accidents to return list of dates
    results = session.query(Traffic.Date).all()
    session.close()

    # Convert list of tuples into normal list
    all_dates = list(np.ravel(results))
    return jsonify(all_dates)

@app.route("/api/v1.0/locations")
def locations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all accidents to return list of genders
    results = session.query(Traffic.Location).all()
    session.close()

    # Convert list of tuples into normal list
    locations = list(np.ravel(results))
    return jsonify(locations)


@app.route("/api/v1.0/addresses")
def addresses():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all accidents to return list of addresses
    results = session.query(Traffic.Address).all()
    session.close()

    # Convert list of tuples into normal list
    all_addresses = list(np.ravel(results))
    return jsonify(all_addresses)


@app.route("/api/v1.0/victimsexes")
def victimsexes():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all accidents to return list of genders
    results = session.query(Traffic.Victim_Sex).all()
    session.close()

    # Convert list of tuples into normal list
    victimsexes = list(np.ravel(results))
    return jsonify(victimsexes)


if __name__ == "__main__":
    app.run(debug=True)
