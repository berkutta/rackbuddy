Rack display
================

This software is used to display system information onto a standard 2x16 display. To get an as much platform independent solution there is the standard Linux i2c interface used.

For talking onto the display there is the following library used: https://github.com/dbrgn/RPLCD

![Demo](https://raw.githubusercontent.com/berkutta/rackbuddy/master/demo.gif "Demo")

Usage
=================

`python main.py`

Install
=================

`$ sudo apt install python-smbus`

`$ sudo pip install RPLCD`

`$ sudo pip install psutil`

