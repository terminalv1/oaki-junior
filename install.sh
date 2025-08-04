#!/bin/bash

echo "🌿 Installing dependencies..."
sudo apt update
sudo apt install -y python3-pip python3-opencv python3-requests python3-flask git libcamera-apps influxdb grafana

echo "📦 Installing Python modules..."
pip3 install pijuice flask

echo "🔧 Enabling services..."
sudo systemctl enable influxdb
sudo systemctl start influxdb
sudo systemctl enable grafana-server
sudo systemctl start grafana-server

echo "🛠️ Setting up systemd services..."
sudo cp systemd/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable motion.service
sudo systemctl enable webui.service
sudo systemctl start motion.service
sudo systemctl start webui.service

echo "⏱️ Installing cron jobs..."
crontab config/crontab.txt

echo "📁 Creating folders..."
mkdir -p ~/timelapse/videos ~/motion ~/config ~/power ~/web_ui

echo "✅ Setup complete. Access web UI at: http://<pi-ip>:8000 and Grafana at http://<pi-ip>:3000"
