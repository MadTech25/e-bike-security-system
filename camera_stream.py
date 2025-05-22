import subprocess
import time

def start_camera_preview():
    print("📷 Starting camera preview. Press Ctrl+C to stop.")
    try:
        subprocess.run([
            "libcamera-vid",
            "-t", "0",
            "--inline",
            "--width", "640",
            "--height", "480",
            "-o", "-"
        ])
    except KeyboardInterrupt:
        print("🛑 Camera preview stopped.")

if __name__ == "__main__":
    start_camera_preview()