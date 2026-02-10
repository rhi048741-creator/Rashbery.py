import time
import board
import busio
import adafruit_tcs34725

i2c=busio.I2C(board.SCL,board.SDA)
#initializ I2C bus
sensor=adafruit_tcs34725.TCS34725(i2c) #initialize sensor

sensor.integration_time=100
sensor.gain=4
print("TCS34725 color sensorRunning.....")
while True:
    r,g,b,c= sensor.color_raw
    print("red= ",r)
    print("green= ",g)
    print("blue= ",b)
    print("clear= ",c)
    time.sleep(1)