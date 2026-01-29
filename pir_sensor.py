import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
while True:
    Pir=GPIO.input(23)
    if Pir==0:
        GPIO.output(22,GPIO.LOW)
        print("led off")
    elif Pir==1:
         GPIO.output(22,GPIO.HIGH)
         print("led on"   )
         