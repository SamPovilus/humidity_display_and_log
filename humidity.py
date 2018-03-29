#!/usr/bin/env python
import serial
import datetime
import time
import psycopg2
import password

def add_humidity(humidity, temp):
                query = """                                                                            
    INSERT INTO                                                                                
        humidity_display_humidity (humidity,temp,log_date,hostname)                                                                         
    VALUES                                                                                     
        (%s, %s, %s, %s)                                                                           
    """
                values = (humidity, temp,"now","piw2")
                cur.execute(query, values)
                conn.commit()

                
conn = psycopg2.connect('host=pib1 user=pi password=' + password.get_password() + ' dbname=humidity_django_db')
cur = conn.cursor()
f = open('/home/pi/temp-humidity.csv', 'a')
ser = serial.Serial('/dev/ttyACM0',9600)
ser2 = serial.Serial('/dev/ttyS0',9600)
brightness_command = "7a"
cursor_command = "79"
decimal_command = "77"
cursor0 = cursor_command + "00"
ser2.write((brightness_command + "02").decode("hex"))
loopcount = 0
while True:

        line = ser.readline()
        humidity2 = line.split()[1].split(":")[1][0:-1]
        tempurature2 = line.split()[0].split(":")[1].strip()[0:-2]
        humi = line.split()[loopcount%2].split(":")[1]
        try:
                ser2.write(("79000"+
                            str(humi[0])+ "0" +
                            str(humi[1])+ "0" +
                            str(humi[3])+ "0" +
                            str(humi[4])).decode("hex"))
                if(loopcount%2==1):
                        ser2.write("7710".decode("hex"))
                else:
                        ser2.write("7700".decode("hex"))
        except TypeError:
                print("couldn't update display")
        loopcount += 1
        if(loopcount % (60) == 0):
                add_humidity(humidity2,tempurature2)
