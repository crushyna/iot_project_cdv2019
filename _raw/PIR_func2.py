import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("PIR Module Test (CTRL+C to exit)")
    time.sleep(4)
    print("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            time.sleep(1)
        else:
            print("No motion!")

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()