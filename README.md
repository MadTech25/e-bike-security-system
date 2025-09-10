# E-Bike Security System ðŸš²ðŸ”’

Smart anti-theft and control system for custom e-bikes.  
Built with ESP32 microcontrollers, modular hardware, and open-source firmware.

---

## ðŸ”§ Features
- **Alarm System** â€” motion/tamper detection with buzzer + flashing LEDs  
- **RFID + Keypad Lock** â€” secure unlock with RFID card or code  
- **GPS Tracking** â€” locate your bike if stolen (NEO-6M GPS)  
- **Wireless Comms** â€” ESP-NOW for board-to-board communication  
- **Expandable** â€” designed for modular add-ons (sensors, displays, etc.)

---

## ðŸ“‚ Repo Structure
- `docs/` â†’ Roadmap, changelog, repo map  
- `firmware/` â†’ ESP32 firmware (ESP32-1, ESP32-2, ESP32-S3 stubs)  
- `hardware/` â†’ wiring templates, enclosure placeholders  
- `media/` â†’ images and demo videos  

---

## ðŸš€ Quickstart
1. Clone the repo:
   ```bash            â† three backticks go here (open the code block)
   git clone https://github.com/MadTech25/e-bike-security-system.git
   cd e-bike-security-system
   ```                â† three backticks go here (close the code block)
2. Open `firmware/esp32-*/examples/` in Arduino IDE or PlatformIO.  
3. Flash one of the stub sketches to your board.  
4. Check `docs/ROADMAP.md` for development phases.



## ?? Appendix

See [Appendix A — Development Incident & Recovery Log](docs/APPENDIX.md) for detailed notes on the 09/10/2025 surge and recovery event.

## ?? Appendices

- [Appendix A — Capstone Documentation](docs/APPENDIX_A.md)
- [Appendix B2 — Development Incident & Recovery Log](docs/APPENDIX_B2.md)

