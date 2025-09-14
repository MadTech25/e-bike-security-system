# Appendix B4 — 09/13/2025
**Topic:** Pedal Assist Sensors (PAS), Controllers, and Hub Communication

## Key Learnings
- **KT V1-2L / V12L PAS sensors**
  - Require a **magnet ring** to function.
  - Install with the **arrow aligned to forward crank rotation**.
  - 1–3 mm gap between magnets and sensor face.
  - Internal hall ICs are fragile and can fail.

- **When PAS stops “talking” to controller**
  - Magnet disc gap too wide/slipped.
  - No 5 V supply from controller.
  - Brake cutoffs/throttle override active.
  - Broken/corroded PAS signal wire.
  - Controller settings ignoring PAS.

- **Hub motor halls vs PAS halls**
  - Hub motor: 3 halls (+5V, GND, 3 signals). One failed hall ? knock/cut-out.
  - PAS: single hall; failure = no cadence pulses.

- **Current hardware status**
  - Motor 1 ? parked (hall issue).
  - Motor 2 ? runs on throttle; baseline for testing.
  - Sensor 1 ? used to work (10s bursts), now dead.
  - Sensor 2 (KT V1-2L) ? incompatible with LY controller or dead.

- **Controller & PAS compatibility**
  - Controller: **LY36V500W** (36 V, 500 W).
  - Battery: 48 V; Motor: 1000 W hub.
  - Mismatch: 36 V controller + 48 V pack.
  - Needs **generic 3-wire cadence PAS**, not KT-specific.

## Reframe / Elite Perspective
- Don’t over-invest in dead $10 PAS units ? swap in a known-good **3-wire cadence PAS**.
- Coils seldom fail; halls/harness do. Test with meter before part swaps.
- Keep the system matched: **48 V battery ? 48 V controller ? 1000 W motor**.
- Throttle-only baseline is enough to advance alarm/security integration.

## Action Items
- Use Motor 2 + throttle as baseline.
- Replace PAS with **3-wire, 12-magnet cadence sensor**.
- Align controller to 48 V if keeping 48 V battery + 1000 W motor.