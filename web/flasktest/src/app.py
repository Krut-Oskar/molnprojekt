from flask import Flask, render_template, redirect, url_for
import requests
import json
import datetime
from dotenv import load_dotenv
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

load_dotenv()
app = Flask(__name__)

keyVaultName = os.getenv("KEY_VAULT_NAME")
KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
retrieved_data = client.get_secret("DATA-URL")
retrieved_api = client.get_secret("API-URL")

@app.route('/')
def index():
    response_func = requests.get(retrieved_data.value)
    func_json = response_func.json()
    for i in func_json:
        temp = i["temperature"]
    if temp > 25:
        return redirect(url_for("bike"))
    else:
        return redirect(url_for("train"))

@app.route('/bike')
def bike():
    response_func = requests.get(retrieved_data.value)
    func_json = response_func.json()
    for i in func_json:
        temp = i["temperature"]
    temp_corr = str.format("{0:.1f}",temp)
    dt = datetime.datetime.now();
    clock = dt.strftime('%H:%M:%S')
    return render_template("bike.html", temp=temp_corr, clock=clock)

@app.route('/train')
def train():
    lista = []
    response_api = requests.get(retrieved_api.value)
    api_json = response_api.json()
    for item in api_json["Departure"]:
        lista.append(item["direction"])
        lista.append(item["time"])
    length = len(lista)
    response_func = requests.get(retrieved_data.value)
    func_json = response_func.json()
    for i in func_json:
        temp = i["temperature"]
    temp_corr = str.format("{0:.1f}",temp)
    dt = datetime.datetime.now();
    clock = dt.strftime('%H:%M:%S')
    return render_template('train.html', lista=lista, clock=clock, temp=temp_corr, length=length)

if __name__ == "__main__":
    app.run(debug=True)