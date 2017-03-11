#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	int count = 1
    print count +' Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
