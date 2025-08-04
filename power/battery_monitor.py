#!/usr/bin/env python3
import time
import json
import subprocess
import requests
from pijuice import PiJuice

# Load config
with open('/home/pi/config/power_config.json') as f:
    config = json.load(f)

pj = PiJuice(1, 0)
charge = pj.status.GetChargeLevel()['data']

print(f"[BatteryMonitor] Charge: {charge}%")

if charge <= config.get("shutdown_threshold", 10):
    msg = f"Battery critical: {charge}%. Shutting down!"
    print(msg)
    if config.get("telegram_alert", True):
        subprocess.run(["python3", "/home/pi/motion/send_telegram.py", msg])
    if config.get("http_alert", True):
        requests.post(config.get("notify_url"), json={"type": "shutdown", "level": charge})
    subprocess.call(["sudo", "shutdown", "-h", "now"])

elif charge <= config.get("warn_threshold", 20):
    msg = f"Battery warning: {charge}%"
    print(msg)
    if config.get("telegram_alert", True):
        subprocess.run(["python3", "/home/pi/motion/send_telegram.py", msg])
    if config.get("http_alert", True):
        requests.post(config.get("notify_url"), json={"type": "warn", "level": charge})
