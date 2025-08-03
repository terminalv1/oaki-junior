#!/usr/bin/env python3
from flask import Flask, send_file, render_template_string
import os
import glob

app = Flask(__name__)

@app.route('/')
def index():
    latest = '/home/pi/timelapse/latest.jpg'
    snapshots = sorted(glob.glob('/home/pi/timelapse/*.jpg'))
    snapshots = [os.path.basename(p) for p in snapshots if 'motion' not in p]
    motions = sorted(glob.glob('/home/pi/timelapse/motion_*.jpg'))
    motions = [os.path.basename(m) for m in motions]

    html = '''
    <h1>Plant Timelapse Snapshot Viewer</h1>
    <h2>Latest Image</h2>
    <img src="/latest.jpg" width="600"><br><br>

    <h2>Time-Lapse Photos</h2>
    <ul>
    {% for file in snapshots %}
      <li><a href="/timelapse/{{file}}">{{file}}</a></li>
    {% endfor %}
    </ul>

    <h2>Detected Motions</h2>
    <ul>
    {% for file in motions %}
      <li><a href="/timelapse/{{file}}">{{file}}</a></li>
    {% endfor %}
    </ul>
    '''
    return render_template_string(html, snapshots=snapshots, motions=motions)

@app.route('/latest.jpg')
def latest_image():
    return send_file('/home/pi/timelapse/latest.jpg', mimetype='image/jpeg')

@app.route('/timelapse/<filename>')
def serve_snapshot(filename):
    path = os.path.join('/home/pi/timelapse', filename)
    return send_file(path, mimetype='image/jpeg')

app.run(host='0.0.0.0', port=8000)
