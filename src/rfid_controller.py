import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class RfidController:
    reader = SimpleMFRC522()

    @staticmethod
    def read_rfid():
        try:
            print('RFID check')
            time.sleep(1)
            while True:
                if RfidController.reader.read():
                    print('Card detected!')
                    # id, text = RfidController.reader.read()
                    # GPIO.cleanup()
                    # return id, text

                else:
                    print('No card!')
                    GPIO.cleanup()

        # finally:
        #   GPIO.cleanup()

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()