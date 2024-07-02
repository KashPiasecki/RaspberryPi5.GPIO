from gpiozero import LED
from time import sleep

led = LED(17)

# Program loop
def loop():
    while True:
        led.on()
        print("On")
        sleep(1)
        led.off()
        print("Off")
        sleep(1)

# Dispose of all opened GPIO
def dispose():
    led.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program
        dispose()
        print("Ending program")