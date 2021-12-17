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
    response_func = requests.get(os.getenv("DATA_URL"))
    func_json = response_func.json()
    for i in func_json:
        temp = i["temperature"]

    lista = []
    response_api = requests.get(os.getenv("API_URL"))
    api_json = response_api.json()
    for item in api_json["Departure"]:
        lista.append(item["time"])
        lista.append(item["direction"])

    return render_template('index.html', lista=lista, temp=temp)

@app.route('/api')
def get_data():
    testList = []
    data = requests.get(os.getenv("API_URL"))
    json_data = data.json()
    for item in json_data["Departure"]:
        testList.append(item["direction"])
        testList.append(item["time"])
    return render_template('api.html', lista=testList)

if __name__ == "__main__":
    app.run(debug=True)