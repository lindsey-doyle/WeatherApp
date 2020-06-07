# path
from flask import Flask, render_template, flash, redirect, url_for, request
from pprint import pprint as pp
import datetime

# should move weather. into src folder at some point 
from weather import query_api, get_time

app = Flask(__name__)

@app.route("/")
def home():
    # TODO - put data in config file 
    return render_template("home.html", data=[
                                        {'name':'San Diego'},
                                        {'name':'San Francisco'}, 
                                        {'name':'Milwaukee'}, 
                                        {'name':'Tijuana'}
                                        ])

@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    #pp(resp)
    if resp:
        data.append(resp)
         # convert sunset time 
        sunset = get_time(data[0]['sys']['sunset'])
        if len(data) != 2:
            error = 'Bad Response from Weather API'
        #else:
            # convert sunset time 
            #sunset = get_time(data[0]['sys']['sunset'])

    return render_template('result.html', data=data, sunset=sunset, error=error)


if __name__ == "__main__":
    app.run(debug=True)
