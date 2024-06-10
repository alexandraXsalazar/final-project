# chatbot/chatbot.py

import os
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from django.conf import settings

lemmatizer = WordNetLemmatizer()

# Construir la ruta absoluta para los archivos
model_path = os.path.join(settings.BASE_DIR, 'finalProject', 'chatbot')

# Cargar los archivos generados en el código anterior
intents = json.loads(open(os.path.join(model_path, 'intents.json')).read())
words = pickle.load(open(os.path.join(model_path, 'words.pkl'), 'rb'))
classes = pickle.load(open(os.path.join(model_path, 'classes.pkl'), 'rb'))
model = load_model(os.path.join(model_path, 'chatbot_model.h5'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res == np.max(res))[0][0]
    category = classes[max_index]
    return category

def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])

def respuesta(message):
    ints = predict_class(message)

    res = get_response(ints, intents)

    print(res)
    return res
