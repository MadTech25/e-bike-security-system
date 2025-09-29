# E-Bike Security System 

Smart anti-theft and control system for custom e-bikes.  
Built with ESP32 microcontrollers, modular hardware, and open-source firmware.

---

##  Features
- **Alarm System**  motion/tamper detection with buzzer + flashing LEDs  
- **RFID + Keypad Lock**  secure unlock with RFID card or code  
- **GPS Tracking**  locate your bike if stolen (NEO-6M GPS)  
- **Wireless Comms**  ESP-NOW for board-to-board communication  
- **Expandable**  designed for modular add-ons (sensors, displays, etc.)

---

##  Repo Structure
- `docs/`  Roadmap, changelog, repo map  
- `firmware/`  ESP32 firmware (ESP32-1, ESP32-2, ESP32-S3 stubs)  
- `hardware/`  wiring templates, enclosure placeholders  
- `media/`  images and demo videos  

---

##  Quickstart
1. Clone the repo:
   ```bash             three backticks go here (open the code block)
   git clone https://github.com/MadTech25/e-bike-security-system.git
   cd e-bike-security-system
   ```                 three backticks go here (close the code block)
2. Open `firmware/esp32-*/examples/` in Arduino IDE or PlatformIO.  
3. Flash one of the stub sketches to your board.  
4. Check `docs/ROADMAP.md` for development phases.



## ?? Appendix

See [Appendix A  Development Incident & Recovery Log](docs/APPENDIX.md) for detailed notes on the 09/10/2025 surge and recovery event.

## ?? Appendices

- [Appendix A  Capstone Documentation](docs/APPENDIX_A.md)
- [Appendix B2  Development Incident & Recovery Log](docs/APPENDIX_B2.md)



## Appendices

- [Appendix A — Capstone Report](docs/APPENDIX_A.md)
- [Appendix B1 — Technical Notes](docs/APPENDIX.md)
- [Appendix B2 — Power Protection & ESP-NOW](docs/APPENDIX_B2.md)
- [Appendix B3 — 3D Printing PLA & Quick References](docs/APPENDIX_B3.md)
- [Appendix B4 — PAS Sensors, Hub Halls, Controller Mismatch](docs/APPENDIX_B4.md)
## 📒 Project Logs & Documentation
- **Weekly Build Logs:** [Sept 15–19, 2025](logs/2025-09-15_weekly.md)
- **Alarm System Tiers:** [Doc](docs/hardware/ALARM_SYSTEM_TIERS.md)
