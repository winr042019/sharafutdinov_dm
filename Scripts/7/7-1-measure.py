import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)

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
    m = []
    t_s = time.time()

    GPIO.output(troyka, 1)
    v = adc()
    while (v < 0.9 * 256):
        m.append(v)
        v = adc()

    GPIO.output(troyka, 0)
    v = adc()
    while (v > 0.1 * 256):
        m.append(v)
        v = adc()

    t_f = time.time()
    t = t_f - t_s

    plt.plot(m)
    plt.show()

    with open("data.txt", "w") as out:
        out.write("\n".join([str(i) for i in m]))
    """with open("settings.txt", "w") as out:
        out.write(f)
        out.write(s)"""

    print("T: {:.3f}".format(t / len(m)))
    print("Total: {:.3f}".format(t))
    print("Freq: {:.3f}".format(len(m) / t))

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
