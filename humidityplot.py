#!/usr/bin/env python
import matplotlib
import matplotlib.pyplot as plt
import re
import datetime
import time

humidityarray = [1]
timearray = []
tempuraturarray = []
with open('temp-humidity.csv') as f:
    lines = f.readlines()
for line in lines:
    if not re.match(r'^\s*$', line):
        linedate = line.split(",")[0]
        try:
            linedateobj = datetime.datetime.fromtimestamp(time.mktime(datetime.datetime.strptime(linedate,"%Y-%m-%d %H:%M:%S.%f").timetuple()))
            print(linedateobj)
            timearray.append(linedateobj)
            locline = line.split(":")[-1].rstrip().translate(None,'%')
            humidityarray.append(locline)
            tempuraturarray.append(line.split(",")[1].split(":")[1].translate(None,'F'))
        except:
            pass
plt.plot_date(matplotlib.dates.date2num(timearray),(humidityarray[0:-1]))
plt.plot_date(matplotlib.dates.date2num(timearray),(tempuraturarray))
#plt.ylabel('some numbers')
plt.show()
