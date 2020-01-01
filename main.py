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
        print('\n---- Hello!')

        print("RFID process start: ")
        p1 = multiprocessing.Process(target=RfidController.read_rfid)
        p1.start()

        time.sleep(0.5)

        print("PIR process start: ")
        p2 = multiprocessing.Process(target=PIRController.read_pir2)
        p2.start()

        time.sleep(0.5)


if __name__ == "__main__":
    Main.main()
