import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
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

    GPIO.output(dac, [int(i) for i in bin(n)[2:].zfill(8)])
    time.sleep(0.01)
    if GPIO.input(comp) == 1:
        n -= 1

    return n


try:
    while True:
        v = adc()
        a = [0] * 8
        i = 0
        while i < 8 * v / 256:
            a[i] = 1
            i += 1
        GPIO.output(leds, a)
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
