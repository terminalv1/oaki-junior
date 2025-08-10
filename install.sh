#!/bin/bash

echo "🌿 Installing dependencies..."
sudo apt update
sudo apt install -y python3-pip python3-opencv python3-requests python3-flask git libcamera-apps 

# influx manual
echo "🌿 Installing influxdb..."
# Add InfluxData signing key
wget -qO- https://repos.influxdata.com/influxdata-archive.key \
  | gpg --dearmor | sudo tee /usr/share/keyrings/influxdata-archive-keyring.gpg >/dev/null

# Add repository for your OS (e.g. bullseye or bookworm)
echo "deb [signed-by=/usr/share/keyrings/influxdata-archive-keyring.gpg] https://repos.influxdata.com/debian $(lsb_release -cs) stable" \
  | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt update
sudo apt install -y influxdb


echo "📦 Installing Python modules..."
# Flask via pip
pip3 install flask --break-system-packages

# PiJuice via GitHub
sudo apt install pijuice-base
sudo apt install pijuice-gui

echo "➕ Adding Grafana APT repository..."
sudo apt install -y software-properties-common wget gnupg2 apt-transport-https
sudo mkdir -p /etc/apt/keyrings
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install -y grafana

echo "🚀 Enabling services..."
sudo systemctl enable influxdb
sudo systemctl start influxdb
sudo systemctl enable grafana-server
sudo systemctl start grafana-server

echo "📦 Creating InfluxDB database..."
influx -execute "CREATE DATABASE plant_timelapse"

echo "📁 Creating folders from current dir..."
mkdir -p ./timelapse/videos ./motion ./config ./power ./web_ui

echo "🛠️ Setting up systemd services..."
sudo cp systemd/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable motion.service
sudo systemctl enable webui.service
sudo systemctl start motion.service
sudo systemctl start webui.service

echo "⏱️ Installing cron jobs..."
crontab config/crontab.txt

echo "✅ Setup complete. Access web UI at: http://<pi-ip>:8000 and Grafana at http://<pi-ip>:3000"
