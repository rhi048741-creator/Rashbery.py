import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP )
led_state=0
while True:
    button=GPIO.input(26)
    if(GPIO.input(26)==0):
        led_state=not led_state
        if led_state:
            GPIO.output(22,GPIO.HIGH)
            GPIO.output(23,GPIO.HIGH)
        else:
            GPIO.output(22,GPIO.LOW)
            GPIO.output(23,GPIO.LOW)
        time.sleep(0.3)
        while(GPIO.input(26)==0):
                pass
        while(GPIO.input(26)==1):
                pass
            