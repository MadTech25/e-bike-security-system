# Appendix A — 09/10/2025 Development Incident & Recovery Log

**Event:** Buck Converter Surge & ESP32-S3 Recovery  

## Context
While testing with the 48 V battery and buck converters, a live disconnect caused a surge event that dropped the ESP32-S3. The board initially appeared dead (no LEDs, no COM port recognition).  

## Sequence of Events
- **Buck Converter Blowout**
  - Disconnecting the buck under load produced a transient spike.
  - Fuse did not clamp fast enough; surge propagated to downstream rail.
  - ESP32-S3 lost visible power (green/orange LEDs off).

- **Isolation & Recovery**
  - All external power (battery, buck) removed.
  - USB-only test bench applied.
  - BOOT + RESET sequence forced the S3 into download mode.
  - Red LED lit; Windows recognized USB Serial Device (COM14).

- **Revalidation**
  - Arduino IDE configured:
    - **Board**: ESP32S3 Dev Module
    - **PSRAM**: OPI PSRAM
    - **Port**: COM14
  - Blink sketch + Serial heartbeat uploaded successfully.
  - Verified communication at 115200 baud.

## Outcome
ESP32-S3 survived the surge event. Board is restored to baseline and functional.  

## Key Lessons
- Live-disconnects on buck converters risk destructive voltage spikes.  
- Software settings cannot disable power LEDs; dark board = rail failure.  
- Always prove rails (VBUS 5 V, regulator 3.3 V) before assuming chip failure.  
- Capture “known-good” Tools settings + blink sketch for quick restoration.  

## Next Actions
- Add surge protection (TVS diode, inline polyfuse, bulk caps).  
- Resume Phase 1 roadmap: I²C scan and UART comms testing.  
