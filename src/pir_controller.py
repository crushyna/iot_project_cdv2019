import RPi.GPIO as GPIO
import time
from src.led_controller import LedController


class PIRController:

    @staticmethod
    def read_pir2():
        GPIO.setmode(GPIO.BOARD)
        PIR_PIN = 40
        GPIO.setup(PIR_PIN, GPIO.IN)
        try:
            print("PIR check")
            time.sleep(1)
            while True:
                if GPIO.input(PIR_PIN):
                    print("Motion detected!")
                    LedController.motion_detected_blink()
                    GPIO.cleanup()
                    time.sleep(1)
                    break
                else:
                    print("no motion!")
                    GPIO.cleanup()
                    time.sleep(1)
                    break

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
