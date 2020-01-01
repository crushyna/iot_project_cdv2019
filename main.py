from src.rfid_controller import RfidController
from src.pir_controller import PIRController
import RPi.GPIO as GPIO
from src.azure_controller import AzureDBController
import time
import signal
import sys
import multiprocessing


# to exit program gracefully
def signal_handler(signal, frame):
    GPIO.cleanup()
    print("Program ended gracefully!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class Main:

    @staticmethod
    def main():
        print('\n---- Hello!')
        time.sleep(1)

        print("RFID process start: ")
        p1 = multiprocessing.Process(target=RfidController.read_rfid)
        p1.start()

        print("PIR process start: ")
        p2 = multiprocessing.Process(target=PIRController.read_pir2)
        p2.start()


if __name__ == "__main__":
    Main.main()
