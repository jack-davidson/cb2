import requests
from config import API_KEY


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ API_KEY + "/classify"

    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify("I dropped my phone in water")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print("result: '%s' with %d%% confidence" % (label, confidence))
