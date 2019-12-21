import RPi.GPIO as GPIO
import time


class LedController:

    @staticmethod
    def test_blink():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)

    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)

    print("LED off")
    GPIO.output(18,GPIO.LOW)

