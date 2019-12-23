import RPi.GPIO as GPIO
import time


class LedController:

    @staticmethod
    def test_blink():
        # YELLOW
        led_test_pin = 11
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_test_pin, GPIO.OUT)
        GPIO.setwarnings(False)

        print(f"Test LED ON; pin {led_test_pin}")
        GPIO.output(led_test_pin, GPIO.HIGH)
        time.sleep(5)

        print("Test LED OFF; pin {led_test_pin}")
        GPIO.output(led_test_pin, GPIO.LOW)
        GPIO.cleanup()

    @staticmethod
    def motion_detected_blink():
        # YELLOW
        led_test_pin = 11
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_test_pin, GPIO.OUT)
        GPIO.setwarnings(False)

        GPIO.output(led_test_pin, GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(led_test_pin, GPIO.LOW)
        GPIO.cleanup()

    @staticmethod
    def access_granted_blink():
        # GREEN
        led_pin = 13
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.setwarnings(False)

        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(2)

        GPIO.output(led_pin, GPIO.LOW)
        GPIO.cleanup()

    @staticmethod
    def access_denied_blink():
        # RED
        led_pin = 15
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.setwarnings(False)

        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(2)

        GPIO.output(led_pin, GPIO.LOW)
        GPIO.cleanup()

# LedController.test_blink()