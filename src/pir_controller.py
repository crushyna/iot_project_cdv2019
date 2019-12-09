import RPi.GPIO as GPIO
import time


class PIRController:

    @staticmethod
    def read_pir2():
        GPIO.setmode(GPIO.BOARD)
        PIR_PIN = 40
        GPIO.setup(PIR_PIN, GPIO.IN)
        try:
            print("PIR check")
            time.sleep(1)
            print("Ready")
            while True:
                if GPIO.input(PIR_PIN):
                    print("Motion detected!")
                    time.sleep(1)
                else:
                    print("No motion!")
                    GPIO.cleanup()
                    break

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
