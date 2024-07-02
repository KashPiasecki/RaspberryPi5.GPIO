from gpiozero import LED
from time import sleep

led1 = LED(14)
led2 = LED(15)
led3 = LED(17)
led4 = LED(18)
led5 = LED(27)

ledArray=[led1, led2, led3, led4, led5]

def translate(number):
    binaryArray = list(f'{number:05b}')
    # Turn on corresponding diodes
    for i in range(len(binaryArray)):
        ledArray[i].off() if int(binaryArray[i]) == 0 else ledArray[i].on()

    print("Translation complete")
    sleep(5)

    for led in ledArray:
        led.off()
        
def loop():
    while True:
        try:
            number = int(input("Provide a number from 0-31: "))
            if number < 0:
                print("Number is negative")
                continue
            elif number > 31:
                print("Number is higher than maximum value")
                continue
            else:
                translate(number)
                continue
        except ValueError:
            print("Nan")

def dispose():
    for led in ledArray:
        led.close()
    
if __name__ == '__main__':
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:
        dispose()
        print("Ending program")