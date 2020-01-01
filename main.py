from src.rfid_controller import RfidController
from src.pir_controller import PIRController
from src.azure_controller import AzureDBController
import time
import signal
import sys
import multiprocessing


# to exit program gracefully
def signal_handler(signal, frame):
    print("Program ended gracefully!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class Main:

    @staticmethod
    def main():
        while 1:
            print('\n---- Hello!')
            p2 = multiprocessing.Process(target=RfidController.read_rfid)
            p2.start()

            # RfidController.read_rfid()
            # PIRController.read_pir2()

            time.sleep(0.1)


if __name__ == "__main__":
    Main.main()
    p1 = multiprocessing.Process(target=PIRController.read_pir2)
    p1.start()
