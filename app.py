from flask import Flask, render_template, url_for, request
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.models import model_from_json
from sklearn.feature_extraction.text import TfidfVectorizer
import sys, os

app = Flask(__name__)

global model, loaded_vec


def load_model():
    # load json and create model
    json_file = open('model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model/model.h5")
    print("Loaded model from disk")
    
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return loaded_model

def preprocess_text(data):
    print(data)
    tfidf =  loaded_vec.transform([data])
    return tfidf.toarray()

model = load_model()
loaded_vec = pickle.load(open("model/feature.pkl", "rb"))


@app.route("/")
def index():
    return render_template('home.html', prediction = -1)

@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['message']
        x = preprocess_text(text)
#         with graph.as_default():
        out = model.predict(x)
        print(out)
        print(np.argmax(out, axis=1))
        # convert the response to a string
        response = np.argmax(out, axis=1)
        return render_template('home.html',prediction = response[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)