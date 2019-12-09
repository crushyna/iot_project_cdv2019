import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


class RfidController:
    reader = SimpleMFRC522()

    @staticmethod
    def read_rfid():
        try:
            print('RFID check')
            id, text = RfidController.reader.read()

        finally:
            GPIO.cleanup()

        return id, text
