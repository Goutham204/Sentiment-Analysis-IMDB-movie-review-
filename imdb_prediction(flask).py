from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json

app = Flask(__name__)

model = load_model('imdb-002.keras')

with open('D:\Python_vscode\jupyter_notebook\imdb.json') as file:
    imdb = file.read()
    token = tokenizer_from_json(imdb)

def preprocess_text(text, max_length=20):
    sequ = token.texts_to_sequences([text])
    pad = pad_sequences(sequ, maxlen = max_length, padding = 'post', truncating = 'post')
    return pad

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods =['POST'])

def predict():
    review = request.form['review']
    processed_review = preprocess_text(review)

    prediction = model.predict(processed_review)[0][0]
    if prediction >= 0.5:
        sentiment = "Positive"
    else:
        "Negative"
    
    return render_template('index.html', review=review, sentiment=sentiment, probability=round(prediction,2))

if __name__ == '__main__':
    app.run(debug=True)