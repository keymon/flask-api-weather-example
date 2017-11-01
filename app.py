from flask import Flask
import os
import requests
import json


WORLDWEATHERONLINE_WEATHER_ENDPOINT = \
    'http://api.worldweatheronline.com/premium/v1/weather.ashx'
WORLDWEATHERONLINE_API_KEY = \
    os.environ.get('WORLDWEATHERONLINE_API_KEY', 'undefined')


app = Flask(__name__)


@app.route('/')
def root():
    return "weather app"


@app.route('/temp')
def temp():
    params = {
        'key': WORLDWEATHERONLINE_API_KEY,
        'q': 'London',
        'format': 'json'
    }
    response = requests.get(WORLDWEATHERONLINE_WEATHER_ENDPOINT, params=params)
    response.raise_for_status()
    temp = response.json()['data']['current_condition'][0]['temp_C']

    return json.dumps({'temp': temp})


if __name__ == '__main__':
    app.run()
