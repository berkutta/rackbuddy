#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from RPLCD.i2c import CharLCD

from RPLCD import Alignment, CursorMode, ShiftMode
from RPLCD import cursor
from RPLCD import BacklightMode

import socket
import psutil
import time
import os

try:
    input = raw_input
except NameError:
    pass

try:
    unichr = unichr
except NameError:
    unichr = chr


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

lcd = CharLCD(address=0x3F, port=1);

while(True):
	lcd.clear()
	lcd.cursor_pos = (0, 0)
	lcd.write_string(socket.gethostname())
        lcd.cursor_pos = (1, 0)
        lcd.write_string(socket.gethostbyname(socket.gethostname()))
	time.sleep(2)

        lcd.clear()
        lcd.cursor_pos = (0, 0)
        lcd.write_string("CPU: " + str(psutil.cpu_percent()) + '%')
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Temp.: " + getCPUtemperature() + u"\u00b0" + 'C')
        time.sleep(2)

