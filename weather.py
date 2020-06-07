import datetime
import os 
import pytz
import requests
import math

API_KEY = '4664cd649463bbca3ec0363149008560'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=imperial&appid={}')

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
        #print(data)
    except Exception as exc:
        #print(exc)
        data = None
    return data

def get_time(uTime):
                #let dt = new Date(unixTime * 1000)
                #dt = datetime(unixTime*1000)
                #let h = dt.getHours()
                #h = 
                #let m = "0" + dt.getMinutes()
                #let t = h + ":" + m.substr(-2)
                dTime = datetime.datetime.fromtimestamp(uTime).strftime('%H:%M')#.strftime('%Y-%m-%d %H:%M:%S')
                return dTime