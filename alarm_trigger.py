import time
from gpiozero import Buzzer, LED, MotionSensor

# Define your GPIO pins
BUZZER_PIN = 17
LED_PIN = 27
PIR_PIN = 4

buzzer = Buzzer(BUZZER_PIN)
led = LED(LED_PIN)
pir = MotionSensor(PIR_PIN)

def alert_sequence():
    print("🚨 Motion detected! Triggering alarm...")
    led.on()
    buzzer.on()
    time.sleep(5)
    buzzer.off()
    led.off()

def main():
    print("🔒 Alarm system armed. Waiting for motion...")
    while True:
        pir.wait_for_motion()
        alert_sequence()
        time.sleep(1)  # Cooldown period

if __name__ == "__main__":
    main()