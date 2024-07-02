from gpiozero import InputDevice
from time import sleep
from os import system

input = InputDevice(21)

def loop():
    while True:
        if (input.is_active):
            print("POWAAAAAAAAAH")
            print(f"Current input value: {input.value}")
            sleep(0.25)
            system('cls||clear')
        else:
            print("No powah :(")
            print(f"Current input value: {input.value}")
            sleep(0.25)
            system('cls||clear')

def dispose():
    input.close()

if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        dispose()
        print("Ending program")