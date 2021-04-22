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
    categories_responses = [{"Category": "InternetError", "Response": "Please Use This Official Verizon TroubleShooter To Fix Your Internet Issue (https://www.verizon.com/foryourhome/vzrepair/flowengine/UFDService.aspx?Keyword=FIX_CCON)."}, 
                            {"Category": "EndOfConversation", "Response": "We are glad that you got the help you needed, bye!"},
                            {"Category": "CustomerNeedsHelp", "Response": "We hear your concerns about not being able to reach customer service, and are forwarding you to an expert."},
                            {"Category": "BillingError", "Response": "Please Use This Guide To Pay Your Bill (https://www.verizon.com/support/residential/account/pay-bill/how-to)."},
                            {"Category": "InternetSpeedError", "Response": "Please Use This Speed Test (https://www.verizon.com/speedtest/) while I forward you to an expert!"},
                            {"Category": "CableError", "Response": "Please Use This Official Verizon TroubleShooter To Fix Your Cable/TV issue (https://www.verizon.com/business/support/fios-tv/troubleshooting)."}]

    for category_response in categories_responses:
        category = category_response["Category"]
        response = category_response["Response"]

        if label == category and confidence > 10:
            return response

    return "I'm sorry, I can't understand. You will be forwarded to a human expert soon."


print("Welcome To The Version Service Chatbot! Presss Ctrl-C To Quit:")
while True:
    model_input = classify(input("> "))

    label = model_input["class_name"]
    confidence = model_input["confidence"]
    
    print(respond(label, confidence))
