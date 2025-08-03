#!/bin/bash

echo "🔧 Installing required packages..."
sudo apt update
sudo apt install -y python3 python3-pip python3-flask libcamera-apps fswebcam

echo "📦 Installing Python packages..."
pip3 install requests opencv-python-headless

echo "📁 Creating directories..."
mkdir -p ~/timelapse ~/motion ~/web_ui ~/config

echo "📂 Copying files..."
cp timelapse/*.sh ~/timelapse/
cp motion/motion_detect.py ~/motion/
cp web_ui/server.py ~/web_ui/
cp config/motion-config.json ~/config/
crontab config/crontab.txt

echo "🛠️ Setting executable permissions..."
chmod +x ~/timelapse/*.sh ~/motion/motion_detect.py ~/web_ui/server.py

echo "✅ Setup complete. You can now:"
echo "Start web server: python3 ~/web_ui/server.py"
echo "Start motion detection: python3 ~/motion/motion_detect.py &"
