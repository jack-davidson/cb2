import requests

with open("apikey", "r") as f:
    API_KEY = f.read()
    f.close()

API_URL = "https://machinelearningforkids.co.uk/api/scratch/" + API_KEY + "/classify"


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    response = requests.get(API_URL, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify("")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print("result: '%s' with %d%% confidence" % (label, confidence))
