#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
libcamera-still -o /home/pi/timelapse/$DATE.jpg --width 1920 --height 1080 --nopreview
ln -sf /home/pi/timelapse/$DATE.jpg /home/pi/timelapse/latest.jpg
