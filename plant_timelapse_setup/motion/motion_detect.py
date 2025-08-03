#!/usr/bin/env python3
# Placeholder: Detect motion using OpenCV
# Save result + send HTTP notification if motion of interest is found
import cv2
import requests
import time

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Fake motion detection condition for now
    if ret and int(time.time()) % 60 == 0:
        print("Motion detected: Human")
        cv2.imwrite("/home/pi/timelapse/motion.jpg", frame)
        requests.post("https://example.com/motion-alert", json={"type": "human", "timestamp": time.time()})
    time.sleep(5)
