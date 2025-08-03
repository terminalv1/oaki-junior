#!/bin/bash
LOGFILE="/home/pi/timelapse/system_stats.log"
DATE=$(date +"%Y-%m-%d %H:%M:%S")
TEMP=$(vcgencmd measure_temp | cut -d '=' -f2)
VOLT=$(vcgencmd measure_volts | cut -d '=' -f2)
echo "$DATE | Temp: $TEMP | Voltage: $VOLT" >> $LOGFILE
