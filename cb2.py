#!/usr/bin/env python3
import requests
import json
from config import API


with open("data.json", "r") as data_fp:
    chat_data = json.load(data_fp)
    data_fp.close()


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    response = requests.get(API.URL, params={"data": text})
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


while True:
    query = input("> ")
    response = classify(query)
    print(response["class_name"])
