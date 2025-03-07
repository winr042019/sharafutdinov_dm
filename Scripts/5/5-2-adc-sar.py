import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def dectobin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def adc():
    n = 128
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 64
    else:
        n -= 64
    
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 32
    else:
        n -= 32
    
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 16
    else:
        n -= 16
    
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 8
    else:
        n -= 8
    
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 4
    else:
        n -= 4
    
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 2
    else:
        n -= 2
    
    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 0:
        n += 1
    else:
        n -= 1

    return n

try:
    while True:
        v = adc()
        print("Value: {}; voltage: {:.3f}".format(v, v / 256 * 3.3))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
