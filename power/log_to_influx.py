#!/usr/bin/env python3
from pijuice import PiJuice
from datetime import datetime
import requests

pj = PiJuice(1, 0)
charge = pj.status.GetChargeLevel()['data']
status = pj.status.GetStatus()['data']
vbat = pj.status.GetBatteryVoltage()['data']

line = f"battery status={status.get('powerInput', 'unknown')},charge={charge},vbat={vbat}"
r = requests.post("http://localhost:8086/write?db=plant_timelapse", data=line)

print("[Logger] Sent to Influx:", line)
