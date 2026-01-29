import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
count=0
while True:
    count+=1
    Button1=GPIO.input(26)
    Button2=GPIO.input(19)
    if Button1==0:
        GPIO.output(22,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(0.5)
        print("led on")
    elif Button2==0:
        GPIO.output(22,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        print("led off")
    print(count)