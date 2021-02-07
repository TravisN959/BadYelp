from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import requests
import json
import yelpRequest
import googleRequest

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']#gets content input from the form
        task_location = request.form['location']
        businessesFromYelp = yelpRequest.searchBusinesses(task_content, task_location)
        disanceDict = {}
        for biz in businessesFromYelp:
            minutes = googleRequest.getMinutes(task_location, biz['location']["display_address"])
            disanceDict[biz["name"]] = minutes

        try:
            
            return render_template('search.html', businesses= businessesFromYelp, searchLocation=task_location, distances = disanceDict)
        except:
            return 'There was an error searching your task'

    else:#page refreshed/ reloaded so will output the template.
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)