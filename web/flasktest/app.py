from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/asd/')
def get_data():
    r = requests.get("http://127.0.0.1:7071/api/GetCosmosDB")
    r_json = r.json()
    temp = r_json.get("temperature")
    ts = r_json.get("_ts")
    