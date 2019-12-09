import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 21
GPIO.setup(PIR_PIN, GPIO.IN)


class PIRController:

    @staticmethod
    def read_pir2():
        try:
            print("PIR check")
            if GPIO.input(PIR_PIN):
                print("Motion detected!")
                time.sleep(1)

        finally:
            GPIO.cleanup()
