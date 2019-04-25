#!/usr/bin/env python
import minimalmodbus
import time
import urllib3
from time import gmtime, strftime
from urllib.request import urlopen
minimalmodbus.BAUDRATE = 19200

# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

while True:
    # Register number, number of decimals, function code
    idn = instrument.read_register(1, 0, 3)
    locale = instrument.read_register(0, 0, 3)
    wl = (instrument.read_register(0, 0, 4) -24267)/1000*26.5/18.8
    temp = instrument.read_register(1, 0, 4)
    timeQ = strftime("%Y%m%d%H%M%S")
    print('id='+str(idn))
    print('location='+str(locale))
    print('water level='+str(wl))
    print('temperature='+str(temp))

    url = 'http://ec2-54-175-179-28.compute-1.amazonaws.com/update_general.php?site=Mucha&time='+str(timeQ)+'&weather=0&id=6999&air=0&acceleration=0&cleavage=0&incline=0&field1='+str(wl)+'&field2=0&field3=0'
    res = urlopen(url).read()
    print(res)
    time.sleep(10)
