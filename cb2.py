from mltext import classifyText, storeText
from mlmodel import trainModel, checkModel
import requests


with open("apikey", "r") as f:
    API_KEY = f.read()
    f.close()

test_text = "The text that you want to test"

# CHANGE THIS to the text that you want to add
# to your project training data
training_text = "The text that you want to store"

# CHANGE THIS to the training bucket to add the
# training example to
training_label = "questions"

# remove the comment on the next line to use this
storeText(API_KEY, training_text, training_label)
