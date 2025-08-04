#!/bin/bash
# Save 10-second video with timestamp
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
DIR="/home/pi/timelapse/videos"
mkdir -p "$DIR"
libcamera-vid -t 10000 -o "$DIR/motion_$DATE.h264" --nopreview
