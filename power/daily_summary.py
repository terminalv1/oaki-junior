#!/usr/bin/env python3
import os
import subprocess
import requests
from datetime import datetime

today = datetime.now().date()
motion_dir = "/home/pi/timelapse"
videos_dir = "/home/pi/timelapse/videos"
log_path = "/home/pi/timelapse/system_stats.log"
summary_file = f"/home/pi/timelapse/daily_summary_{today}.txt"

motions = [f for f in os.listdir(motion_dir) if f.startswith("motion_") and today.isoformat() in f]
videos = [f for f in os.listdir(videos_dir) if today.isoformat() in f]

try:
    with open(log_path, 'r') as f:
        logs = [line for line in f.readlines() if today.isoformat() in line]
except:
    logs = []

# Write summary to file
with open(summary_file, 'w') as f:
    f.write(f"📅 Summary for {today}\n")
    f.write(f"🧠 Motions detected: {len(motions)}\n")
    f.write(f"🎥 Videos recorded: {len(videos)}\n")
    f.write(f"📈 Log entries: {len(logs)}\n")
    f.write("\nRecent logs:\n" + "".join(logs[-10:]))

# Send summary via Telegram
msg = f"📅 {today} Summary:\n🧠 Motions: {len(motions)}\n🎥 Videos: {len(videos)}\n📈 Logs: {len(logs)}"
subprocess.run(["python3", "/home/pi/motion/send_telegram.py", msg])

# Log to InfluxDB
line = f"daily_summary motions={len(motions)},videos={len(videos)},logs={len(logs)}"
requests.post("http://localhost:8086/write?db=plant_timelapse", data=line)

print("[Summary] Report complete and sent.")
