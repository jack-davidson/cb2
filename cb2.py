import requests
import tokens

key = input("api key:")
url = "https://machinelearningforkids.co.uk/api/scratch/" + tokens.key + "/classify"


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):

    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


while True:
    model_input = classify(input("> "))

    label = model_input["class_name"]
    confidence = model_input["confidence"]

    print(label)
