#!/usr/bin/env python
import serial
#import datetime
from datetime import datetime
import time
import psycopg2
import password
import codecs
from influxdb import InfluxDBClient

client = InfluxDBClient("nas2",8086,"climate")

ser = serial.Serial('/dev/ttyACM0',9600)
ser2 = serial.Serial('/dev/ttyS0',9600)
brightness_command = "7a"
cursor_command = "79"
decimal_command = "77"
cursor0 = cursor_command + "00"
ser2.write(codecs.decode((brightness_command + "02"),"hex"))
loopcount = 0

while True:

        line = ser.readline().decode()
        humidity2 = line.split()[1].split(":")[1][0:-1]
        tempurature2 = line.split()[0].split(":")[1].strip()[0:-2]
        print("humidity2:" + humidity2);
        print("temp2:" +  tempurature2);
        
        humi = line.split()[loopcount%2].split(":")[1]
        print(humi[1])
        print(humi[2])
        print(humi[3])
        print(humi[4])

        try:
                ser2.write(("79000"+
                            str(humi[0])+ "0" +
                            str(humi[1])+ "0" +
                            str(humi[3])+ "0" +
                            str(humi[4])).encode())
                            #codecs.decode(str(humi[4]).strip(),"hex")))
                if(loopcount%2==1):
                        ser2.write(codecs.decode("7710","hex"))
                else:
                        ser2.write(codecs.decode("7700","hex"))
        except TypeError as e:
                print("couldn't update display")
                print(e)
        loopcount += 1
        if(loopcount % (60) == 2):
                client.write_points([{"measurement":"climate","tags":{"host":"pi_pressure_humidity"},"fields":{'humidity':float(humidity2),'tempurature':float(tempurature2)},"time":datetime.now()}],time_precision='s',database='climate')


