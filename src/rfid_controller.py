import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class RfidController:
    reader = SimpleMFRC522()

    @staticmethod
    def read_rfid():
        try:
            print('RFID check')
            if RfidController.reader.read():
                id, text = RfidController.reader.read()
                GPIO.cleanup()
                return id, text

            else:
                GPIO.cleanup()

        finally:
            GPIO.cleanup()