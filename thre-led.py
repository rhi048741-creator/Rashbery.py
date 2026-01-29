import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
count=0
try:
    while True:
        count+=1
        GPIO.output(22,GPIO.HIGH)
        time.sleep(0.5)
        print("led off")
        GPIO.output(22,GPIO.LOW)
        time.sleep(0.5)
        print("led on")
        print(count)
except keyboardinterrupt:
    print("program stopped")
finally:
    GPIO.cleanup()
    