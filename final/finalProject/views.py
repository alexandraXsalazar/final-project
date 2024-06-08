import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cycle, Pc, Student, Staff, Attendance, StaffFeedback, StuFeedback, User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password, make_password
import os


lemmatizer = WordNetLemmatizer()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'intents.json')) as file:
    intents = json.load(file)

with open(os.path.join(BASE_DIR, 'words.pkl'), 'rb') as file:
    words = pickle.load(file)

with open(os.path.join(BASE_DIR, 'classes.pkl'), 'rb') as file:
    classes = pickle.load(file)

model = load_model(os.path.join(BASE_DIR, 'chatbot_model.h5'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
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
    max_index = np.argmax(res)
    category = classes[max_index]
    return category


def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            return random.choice(i['responses'])


@csrf_exempt
def duckBot(request):
    if request.method == 'POST':
        message = json.loads(request.body)['message']
        ints = predict_class(message)
        res = get_response(ints, intents)
        return JsonResponse({'response': res})
    return render(request, 'duckBot.html')


def index(request):
    return render(request, "index.html")

@csrf_exempt
def loginStaff(request):
    if request.method == 'POST':
        username = request.POST.get('logname')
        password = request.POST.get('logpass')
        rolestaff = request.POST.get('lgStaff')
        rolest = request.POST.get('lgStudent')

        if not (username and password):
            return render(request, 'login.html', {'error_message': 'Username and password are required'})

        if not (rolestaff or rolest):
            return render(request, 'login.html', {'error_message': 'Role selection is required'})

        if rolestaff == "staff":
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})

            try:
                staff_user = Staff.objects.get(user=user)
                return render(request, "layoutstaff.html")
            except Staff.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Invalid staff credentials'})

        elif rolest == "student":
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'login.html', {'error_message': 'Invalid username or password'})

            try:
                student_user = Student.objects.get(user=user)
                return render(request, "layotstu.html")
            except Student.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Invalid student credentials'})

        else:
            return render(request, 'login.html', {'error_message': 'Invalid role'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    # Cierra la sesión de manera segura
    logout(request)
    # Evita el almacenamiento en caché de la página de inicio después del cierre de sesión
    response = HttpResponseRedirect(reverse("index"))
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def staffinfo(request):
    staffs = Staff.objects.all()
    return render(request, "staffinfo.html", {"staffs": staffs})

def studentinfo(request):
    students = Student.objects.all()
    return render(request, "staffinfo.html", {"students": students})

def game_view(request):
    return render(request, 'game.html')
