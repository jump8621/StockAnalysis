from flask import Flask
import sqlalchemy
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'DATABASE_URL', 'sqlite:///stanalysis.sqlite')

db = SQLAlchemy(app)

# # Reflect Existing Database Into a New Model
# Base = automap_base()
# # Reflect the Tables
# Base.prepare(db.engine, reflect=True)

# # Save References to Each Table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples

class stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    stname = db.Column(db.String)
    country = db.Column(db.String)

class ge(db.Model):
    timestamp = db.Column(db.Integer, primary_key=True)
    open = db.Column(db.Float)   
    low = db.Column(db.Float)   
    high = db.Column(db.Float)   
    close = db.Column(db.Float)   
    volume = db.Column(db.Float)   


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/tasks')
def getTasksPostgres():
    stocks = db.session.query(stock)
    print(stocks)
    data = []

    for things in stocks:
        item = {
            'id': things.id,
            'description': things.description,
            'stname': things.name,
            'country': things.country
        }
        data.append(item)

    return jsonify(data)


@app.route('/api/candlestick')
def getCandlestick():
    candlesticks = db.session.query(ge)
    print(candlesticks)
    data = []

    for task in candlesticks:
        item = {
            'timestamp' : task.timestamp,
            'open' : task.open,   
            'low' : task.low,   
            'high' : task.high,   
            'close' : task.close,   
            'volume' : task.volume
        }
        data.append(item)

    return jsonify(data)

# so if we connect the info from the jupyter notebook or website 
# directly to the db and give it a sqlite name. then pull in the 
# results with a session.query() similiar to activity 10.3.10  passengers
# the main.js can activate the app.route with a button click
# function handle submit will activate d3.json(api/candlestick).then data
# which will load the data into the candlestick format and plotly format?


if __name__ == "__main__":
    app.run(debug=True)