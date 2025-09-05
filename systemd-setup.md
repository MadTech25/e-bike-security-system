# Auto-Start E-Bike Security Services with systemd

This guide explains how to auto-run each Raspberry Pi script at boot using `systemd`.

---

## 🔧 1. Create a Service for GPS Tracking

```bash
sudo nano /etc/systemd/system/gps-tracker.service
```

Paste:
```ini
[Unit]
Description=E-Bike GPS Tracker
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/raspberrypi/e-bike-security-system/pi/gps_tracker.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

---

## 🚨 2. Create a Service for the Alarm

```bash
sudo nano /etc/systemd/system/alarm.service
```

Paste:
```ini
[Unit]
Description=E-Bike Motion Alarm
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/raspberrypi/e-bike-security-system/pi/alarm_trigger.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

---

## 📷 3. (Optional) Auto-Run Camera Stream

```bash
sudo nano /etc/systemd/system/camera-stream.service
```

Paste:
```ini
[Unit]
Description=E-Bike Camera Stream
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/raspberrypi/e-bike-security-system/pi/camera_stream.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

---

## ⚙️ 4. Enable Services

```bash
sudo systemctl daemon-reload
sudo systemctl enable gps-tracker.service
sudo systemctl enable alarm.service
sudo systemctl enable camera-stream.service
```

---

## ✅ To Start or Stop Manually

```bash
sudo systemctl start gps-tracker.service
sudo systemctl stop alarm.service
sudo systemctl status camera-stream.service
```