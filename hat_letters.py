#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

x=(255, 0, 0)
y=(255, 255, 255)
z=(0, 0, 255)

sense.show_letter("H", x)
time.sleep(1)
sense.show_letter("i", y)
time.sleep(1)
sense.show_letter("!", z)
time.sleep(1)

sense.clear()
