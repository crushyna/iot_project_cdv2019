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
                id = reader.read_no_block()
                if id is None:
                    id = id = reader.read_no_block()
                    if id is None:
                        print('no chip present')
                        time.sleep(1)
                    # id, text = RfidController.reader.read()
                    # GPIO.cleanup()
                    # return id, text

                else:
                    print('Card detected!')
                    time.sleep(2)
                    GPIO.cleanup()
                    break

        # finally:
        #   GPIO.cleanup()

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
