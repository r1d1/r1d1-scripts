#!/usr/bin/env python

from flask import Flask
from flask import url_for
from flask import render_template
from flask import request

from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)
'''
@app.route("/")
def index():
    return "<p>Hello, tout le monde!</p>"

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {escape(name)}!"
'''

@app.route("/game")
def interface(gui=None):
    return render_template('interface.html', guitype=gui)

@app.route("/about")


@app.route("/banane")
def banane():
    return 'banane1'

with app.test_request_context():
    print(url_for('banane'))
    print(request)
