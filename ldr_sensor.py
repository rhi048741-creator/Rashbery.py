import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
while True:
    Ldr=GPIO.input(26)
    if(Ldr==1):
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(19,GPIO.HIGH)
        time.sleep(0.5)
        print("DARK")
    if(Ldr==0):
        GPIO.output(17,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.5                                                                                               )
        print("light")
clenup()        