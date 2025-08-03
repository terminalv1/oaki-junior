#!/usr/bin/env python3
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Plant Timelapse</h1>
    <img src="/latest.jpg" width="640">
    '''

@app.route('/latest.jpg')
def latest_image():
    return send_file('/home/pi/timelapse/latest.jpg', mimetype='image/jpeg')

@app.route('/log')
def log():
    try:
        with open('/home/pi/timelapse/log.txt') as f:
            return '<pre>' + f.read() + '</pre>'
    except:
        return "No log available."

app.run(host='0.0.0.0', port=8000)
