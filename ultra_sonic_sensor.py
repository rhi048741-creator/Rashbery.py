import RPi.GPIO as GPIO
import time

trig=23
echo=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
while True:
    GPIO.output(trig,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig,GPIO.LOW)
    while GPIO.input(echo)==0:
        start_time=time.time()
    while GPIO.input(echo)==1:
        end_time=time.time()
    duration=end_time - start_time
    distance=((duration*34300)/2)
    distancem=round(distance,2)
    print(f"Distance is {distancem} cm")
#     time.sleep(0.1)
