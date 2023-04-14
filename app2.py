from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from datetime import datetime, date, time
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # объект


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/about.html')  # отслеживание
def about():
    return render_template("about.html")  # "Aboutasdfasdf"


@app.route('/brands.html')  # отслеживание
def brands():
    return render_template("brands.html")  # "Aboutasdfasdf"


@app.route('/Nike.html')  # отслеживание
def Nike():
    return render_template("Nike.html")  # "Aboutasdfasdf"


@app.route('/header.html')  # отслеживание
def header():
    return render_template("header.html")


@app.route('/footer.html')  # отслеживание
def footer():
    return render_template("footer.html")


if __name__ == '__main__':
    app.run(debug=True)  # команда запускает локальный сервер, ошибки выводятся на сайт
