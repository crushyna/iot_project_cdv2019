import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    print("Motion detected!!!")

print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print("Ready!")

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(2)
except KeyboardInterrupt:
               print("Quit")
               GPIO.cleanup()