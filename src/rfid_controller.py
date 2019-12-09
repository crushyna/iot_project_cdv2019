import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class RfidController:

    @staticmethod
    def read_rfid():
        try:
            print('RFID check')
            time.sleep(1)
            while True:
                reader = SimpleMFRC522()
                if reader.read_no_block():
                    print('Card detected!')
                    time.sleep(2)
                    # id, text = RfidController.reader.read()
                    # GPIO.cleanup()
                    # return id, text

                else:
                    print('No card!')
                    time.sleep(2)
                    GPIO.cleanup()
                    break

        # finally:
        #   GPIO.cleanup()

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()