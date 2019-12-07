from src.rfid_controller import RfidController
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
        print('Hello!')
        id, text = RfidController.read_rfid()
        print(id, text)
        time.sleep(2)


if __name__ == "__main__":
    main()
