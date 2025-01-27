import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time

# Initialize the HID Keyboard
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Optional: Wait a moment to ensure the device is ready
time.sleep(1)

# Type out the desired phrase
layout.write("subscribe to mellow labs")

# Optionally release all keys (good practice)
keyboard.release_all()
