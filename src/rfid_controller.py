import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from src.led_controller import LedController

class RfidController:

    @staticmethod
    def read_rfid():
        try:
            print('RFID check')
            time.sleep(1)
            while True:
                reader = SimpleMFRC522()
                id = reader.read_id_no_block()
                if id is None:
                    print('no chip present')
                    time.sleep(1)
                    GPIO.cleanup()
                    break

                else:
                    id, text = reader.read()
                    print(id)
                    print(text)
                    LedController.test_blink()
                    time.sleep(1)
                    break

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
