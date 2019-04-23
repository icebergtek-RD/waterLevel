#!/usr/bin/env python
import minimalmodbus
import time

minimalmodbus.BAUDRATE = 19200

# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/tty.usbserial-AI04TZ4M', 1)

while True:
    # Register number, number of decimals, function code
    idn = instrument.read_register(1, 0, 3)
    locale = instrument.read_register(0, 0, 3)
    wl = (instrument.read_register(0, 0, 4) -24267)/1000*26.5/18.8
    temp = instrument.read_register(1, 0, 4)
    print('id='+str(idn))
    print('location='+str(locale))
    print('water level='+str(wl))
    print('temperature='+str(temp))
    time.sleep(1)