import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 40
GPIO.setup(PIR_PIN, GPIO.IN)


class PIRController:

    @staticmethod
    def read_pir2():
        try:
            print("PIR check")
            if GPIO.input(PIR_PIN):
                print("Motion detected!")
                time.sleep(1)

            else:
                GPIO.cleanup()

        finally:
            GPIO.cleanup()
