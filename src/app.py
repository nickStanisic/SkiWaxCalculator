#!/usr/bin/env python3

from flask import Flask, render_template, request
from weather import get_temperatures_for_colorado

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print("hi")
    return render_template('index.html')

    # '''
    # <h1>Howdy</h1>
    #  <form action="/echo_user_input" method="POST">
    #      <input name="user_input">
    #      <input type="submit" value="Submit!">
    #  </form>
    #  '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text