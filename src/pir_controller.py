import RPi.GPIO as GPIO
import time
from src.led_controller import LedController


class PIRController:

    @staticmethod
    def read_pir2():
        PIR_PIN = 40
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIR_PIN, GPIO.IN)
        try:
            print("PIR check")
            while True:
                if GPIO.input(PIR_PIN):
                    print("Motion detected!")
                    LedController.motion_detected_blink()
                    GPIO.cleanup()
                    time.sleep(0.5)
                    break
                else:
                    print("no motion!")
                    GPIO.cleanup()
                    time.sleep(0.5)
                    break

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
