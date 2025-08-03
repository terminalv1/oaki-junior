#!/bin/bash
DATE=$(date +%Y-%m-%d)
DEST="/media/usb/timelapse_backup/$DATE"
mkdir -p "$DEST"
cp /home/pi/timelapse/*.jpg "$DEST"
