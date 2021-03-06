import RPi.GPIO as GPIO
from src.led_controller import LedController


class PIRController:

    @staticmethod
    def read_pir2():
        try:
            print("PIR check")
            while True:
                PIR_PIN = 40
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(PIR_PIN, GPIO.IN)
                if GPIO.input(PIR_PIN):
                    print("Motion detected!")
                    LedController.motion_detected_blink()
                    # time.sleep(0.5)
                    continue
                else:
                    print("no motion!")
                    # time.sleep(0.5)
                    continue

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
