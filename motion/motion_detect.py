#!/usr/bin/env python3
import cv2
import numpy as np
import time
import requests

CONFIDENCE_THRESHOLD = 0.5
TRIGGER_CLASSES = ['person', 'cat', 'dog', 'bird']

net = cv2.dnn_DetectionModel('motion/mobilenet_ssd.pb', 'motion/mobilenet_ssd.pbtxt')
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

with open('motion/coco_labels.txt') as f:
    classes = [line.strip() for line in f.readlines()]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    classIds, confs, bbox = net.detect(frame, confThreshold=CONFIDENCE_THRESHOLD)

    if len(classIds) > 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            label = classes[classId - 1]
            if label in TRIGGER_CLASSES:
                print(f"Motion detected: {label}")
                ts = time.strftime('%Y-%m-%d_%H-%M-%S')
                image_path = f'/home/pi/timelapse/motion_{label}_{ts}.jpg'
                cv2.imwrite(image_path, frame)
                requests.post("https://example.com/motion-alert", json={"type": label, "timestamp": ts})
    time.sleep(5)
