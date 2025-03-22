import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.input(22))
