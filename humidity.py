#!/usr/bin/env python
import serial
import datetime
f = open('/home/pi/temp-humidity.csv', 'a')
ser = serial.Serial('/dev/ttyACM0',9600)
ser2 = serial.Serial('/dev/ttyS0',9600)
brightness_command = "7a"
cursor_command = "79"
cursor0 = cursor_command + "00"
ser2.write((brightness_command + "05").decode("hex"))
loopcount = 0
while True:

        line = ser.readline()

        humi = line.split()[1].split(":")[1]
        ser2.write(("79000"+
                    str(humi[0])+ "0" +
                    str(humi[1])+ "0" +
                    str(humi[3])+ "0" +
                    str(humi[4])).decode("hex"))
        print(humi)
        today = datetime.datetime.now()
        loopcount += 1
        if(loopcount % (20*2) == 0):
            print(line)
            f.write( str(today) + ","+ str(line) + "\n" )
            print("writing")
#        print(line)
#        print(datetime.datetime.now())
