import machine
import dht
from time import sleep

sensor = dht.DHT11(machine.Pin(22))
while True:
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print("Temp:",temp,"Humidity:",humidity)
    sleep(5)