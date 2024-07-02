from gpiozero import LED, Button
from time import sleep

led = LED(17)       # define LED pin according to BCM Numbering
button = Button(18) # define Button pin according to BCM Numbering

def onButtonPressed():  # When button is pressed, this function will be executed
    led.toggle()
    if led.is_lit :
        print("Led turned on >>>")
    else :
        print("Led turned off <<<")    

def loop():
    button.when_pressed = onButtonPressed
    while True:
        sleep(1)

def dispose():
    led.close()
    button.close()  

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        dispose()
        print("Ending program")