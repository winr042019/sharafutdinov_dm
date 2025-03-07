import RPi.GPIO as GPIO
import time

def dectobin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        s = input("Define signal period (q to quit): ")
        if (s == "q"):
            break
        T = int(s)
        for i in range(256):
            dec = dectobin(i)
            GPIO.output(dac, dec)
            time.sleep(T/512)
        for i in range(255, -1, -1):
            dec = dectobin(i)
            GPIO.output(dac, dec)
            time.sleep(T/512)
except TypeError:
    print("Wrong input, rerun")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
