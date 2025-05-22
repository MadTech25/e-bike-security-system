import serial
import time

# Adjust this to your GPS module's serial port
GPS_PORT = "/dev/ttyS0"
BAUD_RATE = 9600

def parse_nmea(sentence):
    if sentence.startswith('$GPGGA') or sentence.startswith('$GPRMC'):
        parts = sentence.split(',')
        if sentence.startswith('$GPRMC') and parts[3] and parts[5]:
            lat = convert_to_degrees(parts[3])
            lon = convert_to_degrees(parts[5])
            if parts[4] == 'S':
                lat = -lat
            if parts[6] == 'W':
                lon = -lon
            return lat, lon
    return None

def convert_to_degrees(raw):
    try:
        d = int(raw[:2])
        m = float(raw[2:])
        return d + (m / 60)
    except:
        return 0.0

def main():
    print("🛰️ Starting GPS tracker...")
    with serial.Serial(GPS_PORT, BAUD_RATE, timeout=1) as gps:
        time.sleep(2)
        while True:
            line = gps.readline().decode('ascii', errors='replace').strip()
            coords = parse_nmea(line)
            if coords:
                lat, lon = coords
                print(f"📍 Latitude: {lat:.6f}, Longitude: {lon:.6f}")
            time.sleep(1)

if __name__ == "__main__":
    main()