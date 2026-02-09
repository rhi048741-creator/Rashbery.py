import time
import board
import adafruit_dht
dht=adafruit_dht.DHT11(board.D4,
                       use_pulseio=False)#d4 is BCM
while True:
    try:
        temperature=dht.temperature
        humidity=dht.humidity
        print(f"Temp:{temperature:.1f}C Humidity:{humidity:.1f}%")
    except RuntimeError as error:
        print(f"Reading Error:{error}")
    time.sleep(2)