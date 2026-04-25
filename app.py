from flask import Flask, render_template, request, redirect, session
from db import *
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

dbo = Database()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('User_name')
    email = request.form.get('User_email')
    password = request.form.get('User_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message='Registration Successful, Kindly login')
    else:
        return render_template('register.html', message='Email already exists')


@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('User_email')
    password = request.form.get('User_password')

    response = dbo.search(email, password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', message='Login Failed')


@app.route('/profile')
def profile():
    if session.get('logged_in') == 1:
        return render_template('profile.html')
    else:
        return redirect('/')


@app.route('/ner')
def ner():
    if session.get('logged_in') == 1:
        return render_template('ner.html')
    else:
        return redirect('/')


def extract_entities(text):
    text = text.title()

    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    chunked = ne_chunk(tagged)

    entities = []
    for subtree in chunked:
        if isinstance(subtree, Tree):
            entity_name = " ".join([word for word, tag in subtree.leaves()])
            entity_type = subtree.label()
            entities.append((entity_name, entity_type))

    return entities


@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    if session.get('logged_in') == 1:
        text = request.form.get('ner_text')
        entities = extract_entities(text)

        return render_template('ner.html', entities=entities, text=text)
    else:
        return redirect('/')


app.run(debug=True)