import matplotlib.pyplot as plt
import re
import datetime
import time

humidityarray = []
timearray = []
with open('temp-humidity.csv') as f:
    lines = f.readlines()
for line in lines:
    if not re.match(r'^\s*$', line):
        linedate = line.split(",")[0]
        try:
            linedateobj = time.mktime(datetime.datetime.strptime(linedate,"%Y-%m-%d %H:%M:%S.%f").timetuple())
            print(linedateobj)
            timearray.append(linedateobj)
            locline = line.split(":")[-1].rstrip().translate(None,'%')
            humidityarray.append(locline)
        except:
            pass
#print(humidityarray)

plt.plot(timearray,humidityarray)
#plt.ylabel('some numbers')
plt.show()
