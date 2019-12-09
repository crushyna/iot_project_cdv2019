from src.rfid_controller import RfidController
from src.pir_controller import PIRController
import time
import signal
import sys


# to exit program gracefully
def signal_handler(signal, frame):
    print("Program ended gracefully!")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    while 1:
        print('\n---- Hello!')
        RfidController.read_rfid()
        # TODO: id & text do bazy danych,
        #  access = zielony, denial = czerwony

        # TODO: równoległa funkcja zbliżeniowa
        PIRController.read_pir2()

        #  if 1 then żółty (5 sec)

        # print(id, text)

        time.sleep(2)


if __name__ == "__main__":
    main()
