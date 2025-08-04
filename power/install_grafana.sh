#!/bin/bash
echo "🔧 Installing InfluxDB and Grafana..."

# Install InfluxDB (v1.x)
sudo apt update
sudo apt install -y influxdb grafana

echo "🚀 Enabling services..."
sudo systemctl enable influxdb
sudo systemctl start influxdb
sudo systemctl enable grafana-server
sudo systemctl start grafana-server

echo "📦 Creating InfluxDB database..."
influx -execute "CREATE DATABASE plant_timelapse"

echo "✅ InfluxDB running on port 8086"
echo "✅ Grafana running on port 3000 (admin/admin)"
