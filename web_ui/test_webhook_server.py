#!/usr/bin/env python3
from flask import Flask, request
import json
import datetime

app = Flask(__name__)

@app.route('/motion-alert', methods=['POST'])
def motion_alert():
    data = request.json
    timestamp = datetime.datetime.now().isoformat()
    with open("received_alerts.log", "a") as f:
        f.write(f"{timestamp} - Received alert: {json.dumps(data)}\n")
    print(f"Alert received: {data}")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
