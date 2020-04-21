# path
#from pprint import pprint as pp
from flask import Flask, render_template, flash, redirect, url_for, request
from weather import query_api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", 
                            data=[
                                {'name':'San Diego'},
                                {'name':'San Francisco'}, 
                                {'name':'Milwaukee'}, 
                                {'name':'Tijuana'}])

@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    
    select = request.form.get('comp_select')
    resp = query_api(select)
    #pp(resp)
    if resp:
        data.append(resp)
        if len(data) != 2:
            error = 'Bad Response from Weather API'
    
    return render_template('result.html', data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
