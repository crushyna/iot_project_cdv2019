import RPi.GPIO as GPIO
import time


class LedController:

    @staticmethod
    def test_blink():
        GPIO.setmode(GPIO.BOARD)
        led_test_pin = 16
        # TODO: unresolvable error, dunno why.
        GPIO.setup(led_test_pin, GPIO.OUT)
        # GPIO.setwarnings(False)
        print("LED on")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(3)
        print("LED off")
        GPIO.output(18, GPIO.LOW)
        # GPIO.cleanup()

GPIO.cleanup()
LedController.test_blink()