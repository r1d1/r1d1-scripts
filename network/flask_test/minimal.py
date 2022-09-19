#!/usr/bin/env python

from flask import Flask
from flask import url_for, redirect
from flask import render_template
from flask import request

from markupsafe import escape

# General script variables
count = 0

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

@app.route("/game", methods=['POST', 'GET'])
def interface(gui=None, action=None):
    print(request.method)
    act = 1
    if request.method == 'POST':
        act = request.form['action_btn']
        print(request.form['action_btn'])
        print(request.form.getlist('choice'))
        #print(request.form['action_play'])
        #print(request.form['action_discard'])
        #print(request.form['action_pass'])
    elif request.method == 'GET':
        act = request.args.get('action_btn')
        print(request.args.get('action_btn'))
        #if request.args.get('action_play'):
        #    act = 1
        #elif request.args.get('action_discard'):
        #    act = 2
        #print(request.args.get('action_play'))
        #print(request.args.get('action_discard'))
        #print(request.args.get('action_pass'))
        
    #return redirect(url_for('success', action=act))
    return render_template('interface.html', guitype=gui, action=act)

@app.route("/interactive_map", methods=['POST', 'GET'])
def interactive_map(action=None, counter=0):
    global count
    act=None
    count += 1
    if request.method == 'POST':
        act = request.form['action_btn']
        print(request.form.getlist('choice'))
    return render_template('interactive_map.html', action=act, counter=count)

@app.route("/success/<action>")
def success(action='none'):
    return "action %s" % action

@app.route("/about")


@app.route("/banane")
def banane():
    return 'banane1'

with app.test_request_context():
    print(url_for('banane'))
    print(request)
