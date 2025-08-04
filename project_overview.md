
# 🌱 Raspberry Pi Timelapse & Monitoring System

A complete off-grid Raspberry Pi 4 system to monitor plant growth with photography, AI motion detection, and environmental logging.

---

## 📷 Features

- **Time-lapse photography** every few minutes
- **AI-based motion detection and classification**
- **PiJuice battery + power input monitoring**
- **Daily video recording on motion triggers**
- **Live Web UI** for viewing, tagging, downloading
- **Grafana dashboard** (battery, motion, logs)
- **Daily summary reports** with Telegram & InfluxDB
- **Wi-Fi auto-connect + USB backup**
- **Public or password-protected access**

---

## 🖼️ System Diagram

![System Diagram](diagram.png)

---

## 📊 Grafana Dashboards

- Battery charge & voltage
- Motion detection over time
- Event breakdown by type
- Daily summary metrics

---

## ⚠️ Alerting System

- Telegram & HTTP notifications:
  - Low battery
  - Motion detections
  - Summary reports

---

## 🛠️ Tech Stack

- **Raspberry Pi OS Lite 64-bit**
- Python 3 + Flask
- OpenCV + MobileNet SSD
- PiJuice HAT
- InfluxDB + Grafana
- Cron + Systemd services

---

## 📦 Setup

See `install.sh` or run:
```bash
./install.sh
```

Ensure you copy all folders to `/home/pi` and create `mobilenet_ssd.pb` weights.

---

## 📁 Folder Structure

```
~/timelapse/             # images, videos, logs
~/motion/                # motion detection scripts
~/web_ui/                # Flask dashboard
~/power/                 # alerts, logging
~/config/                # crontab, settings
~/systemd/               # service units
```

---

## 📤 External Integration

- Public UI via port forward
- Push data to GitHub or external Influx/Grafana
- Can run headless with solar/wind power (via PiJuice)

---
