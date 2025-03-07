import RPi.GPIO as GPIO

def dectobin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        s = input("Enter a number from 0 to 255 (q to exit): ")
        if (s == "q"):
            break
        if (s.isdigit()):
            n = int(s)
            if (n > 255):
                print("The number exceeds DAC capability")
            else:
                dec = dectobin(n)
                GPIO.output(dac, dec)
                print("Supposed voltage: {:.3f}".format(3.3 * n / 256))
            continue
        try:
            n = float(s)
        except ValueError:
            print("Not a number")
        else:
            if (n % 1 != 0):
                print("Not an integer")
            elif (n < 0):
                print("Less than zero")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
