import os
import uuid

from flask import Flask, render_template, request, redirect, url_for, session
import csv
from Person import Person

app = Flask(__name__)
user_info = "user_info"
user_account = "user_account"


@app.route("/")
def home():
    return render_template("main.html", title="home Page")


@app.route("/login")
def login():
    return render_template("login.html", title="Login Page")


@app.route("/signup")
def signup():
    return render_template("signup.html", title="Signup Page")


@app.route("/personal_info")
def information():
    return render_template("personal_info.html", title="info Page")


@app.route("/logged_in")
def logged_in():
    print(session['id'])
    return render_template("logged_in.html", title="Page", NAME=find_name(session['id']))


@app.route('/signup', methods=['POST'])
def signup_handler():
    session['id'] = save_user_info(request.form['email'], request.form['username'], request.form['password'])
    return redirect(url_for('information'))


@app.route('/login', methods=['POST'])
def login_handler():
    ident = verify_user_account(request.form['username'], request.form['password'])
    if ident:
        session['id'] = ident
        return redirect(url_for('logged_in'))
    return "failed"


@app.route('/personal_info', methods=['POST'])
def personal_info_handler():
    Person(request.form['given_name'], request.form['family_name'], request.form['age']).save(session['id'])
    return redirect(url_for('home'))


def find_name(ident):
    with open(user_account, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if ident == row['_id']:
                return row['given_name']
        return 'user not found'


def verify_user_account(username, password):
    with open(user_info, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (username == row['username'] and
                    password == row['password']):
                return row['_id']
    return False


def save_user_info(email, username, password):
    if not os.path.isfile(user_info):
        with open(user_info, 'a', newline="") as csvfile:
            fieldnames = ['email', 'username', 'password', '_id']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()

    ident = str(uuid.uuid4())
    with open(user_info, 'a', newline="") as csvfile:
        fieldnames = ['email', 'username', 'password', '_id']
        writer = csv.DictWriter(csvfile, fieldnames)

        writer.writerow({'email': email, 'username': username, 'password': password, '_id': ident})
        return ident


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
