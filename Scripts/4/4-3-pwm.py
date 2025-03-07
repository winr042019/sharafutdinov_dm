import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)

p = GPIO.PWM(20, 1000)
p.start(0)

try:
    while True:
        s = input("Enter the value of duty cycle (q to exit): ")
        if (s == "q"):
            break
        p.ChangeDutyCycle(int(s))
finally:
    p.stop()
    GPIO.cleanup()
