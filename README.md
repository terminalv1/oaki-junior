
# 🌱 Raspberry Pi Plant Timelapse System

A full-featured timelapse and motion detection system for Raspberry Pi.

---

## 📸 Features

- **Time-lapse photography** every 5 minutes
- **AI motion detection** using MobileNet SSD (person, cat, dog, bird)
- **Telegram + HTTP alerts**
- **Web UI** (Flask-based):
  - View latest image
  - Browse and filter time-lapse + motion captures
  - Tag + annotate images
  - Export as ZIP or MP4
  - Download system logs
  - Slideshow with playback controls
- **Admin login (`admin123`)**
- **USB backup** every night
- **Temperature + voltage logging**
- **Systemd boot startup**
- **Mobile-friendly UI**

---

## 🔧 Installation

1. Flash Raspberry Pi OS Lite (64-bit)
2. Connect via SSH and run:
```bash
wget <URL_TO_SETUP_ZIP>
unzip plant_timelapse_setup.zip
cd plant_timelapse_setup
chmod +x install.sh
./install.sh
```

3. Download MobileNet SSD:
```bash
cd ~/motion
wget https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/ssd_mobilenet_v3_large_coco_2020_01_14.pb -O mobilenet_ssd.pb
wget https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt -O mobilenet_ssd.pbtxt
```

4. Enable auto-start:
```bash
sudo cp systemd/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable motion.service
sudo systemctl enable webui.service
sudo systemctl start motion.service
sudo systemctl start webui.service
```

---

## 🌐 Access

- Visit: `http://<raspberrypi-ip>:8000`
- Admin login: `admin123`

---

## 📤 GitHub Sync

You can push images, logs, or metadata to a private repo:

```bash
cd ~/timelapse
git init
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Optional: save only metadata and log snapshots
echo "*.jpg" > .gitignore

git add .
git commit -m "Initial timelapse upload"
git push -u origin master
```

---

## 🗂️ Folder Structure

```
~/timelapse/         # captured images + logs
~/motion/            # AI detection + telegram
~/web_ui/            # flask dashboard
~/config/            # motion config, crontab
~/systemd/           # startup service files
```

---

## ✨ Customization

- Change admin password in `server.py`
- Adjust motion alert URL in `motion_config.json`
- Use real power sensor (INA219) for accurate readings
- Add DuckDNS or port-forward for public access

---

## 🔒 Security Notes

- Password is hardcoded (`admin123`), change for production
- Consider HTTPS proxy with Nginx for public deployment
- Backup metadata.json regularly if used extensively

---

## License

MIT (or choose your own license)

---
