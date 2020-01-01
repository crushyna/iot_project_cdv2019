import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from src.azure_controller import AzureDBController
from src.led_controller import LedController


class RfidController:

    azuredb1 = AzureDBController()

    @staticmethod
    def read_rfid():
        try:
            print('RFID check')
            while True:
                reader = SimpleMFRC522()
                id = reader.read_id_no_block()
                if id is None:
                    print('no chip present')
                    time.sleep(0.1)
                    GPIO.cleanup()
                    continue

                else:
                    # when card is detected:
                    card_id, card_text = reader.read()
                    user_access = AzureDBController.check_user_access(card_id, card_text)

                    # check is user has access ([HasAccess] column)
                    if user_access:
                        AzureDBController.switch_user_status(card_id, card_text)
                        LedController.access_granted_blink()
                    else:
                        print("No access!")
                        LedController.access_denied_blink()
                        time.sleep(1)

                    continue

        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()
