#!/usr/bin/env python3
import requests
import tokens

url = "https://machinelearningforkids.co.uk/api/scratch/" + tokens.key + "/classify"


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):

    response = requests.get(url, params={"data": text})

    if response.ok:
        response_data = response.json()
        top_match = response_data[0]
        return top_match
    else:
        response.raise_for_status()


def respond(label, confidence):
    categories_responses = [
        {
            "Category": "EndOfConversation",
            "Response": "We are glad that you got the help you needed, bye!"
        }
    ]
    for category_response in categories_responses:
        category = category_response["Category"]
        response = category_response["Response"]

        if label == category and confidence > 35:
            return response

    return "I'm sorry, I can't understand. You will be forwarded to a human expert soon."


print("Welcome To The Version Service Chatbot! Presss Ctrl-C To Quit:")
while True:
    model_input = classify(input("> "))

    label = model_input["class_name"]
    confidence = model_input["confidence"]

    print(respond(label, confidence))
