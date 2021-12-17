from flask import Flask, render_template
import requests
import json
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def get_data():
    testList = []
    data = requests.get(os.getenv("API_URL"))
    json_data = data.json()
    for item in json_data["Departure"]:
        testList.append(item["time"])
        testList.append(item["direction"])
        
        
    # temp = data["temperature"]
    # ts = datetime.datetime.fromtimestamp(data["_ts"])
    return render_template('api.html', lista=testList)

if __name__ == "__main__":
    app.run(debug=True)