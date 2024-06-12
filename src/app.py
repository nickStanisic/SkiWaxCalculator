#!/usr/bin/env python3

from flask import Flask, render_template, request
from weather import calculatePoints

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    data = None
    if request.method == 'POST':
        lowTemp = request.form['lowTemp']
        highTemp = request.form['highTemp']
        startTime = request.form['startTime']
        endTime = request.form['endTime']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        data = calculatePoints(lowTemp, highTemp, startTime, endTime, startDate, endDate)
    return render_template('index.html', data=data)

    # '''
    # <h1>Howdy</h1>
    #  <form action="/echo_user_input" method="POST">
    #      <input name="user_input">
    #      <input type="submit" value="Submit!">
    #  </form>
    #  '''