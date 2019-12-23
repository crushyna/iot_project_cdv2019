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
            while True:
                if GPIO.input(PIR_PIN):
                    print("Motion detected!")
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
