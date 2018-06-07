#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
x=random.randint(1,7)
y=random.randint(1,7)
sense.set_pixel(x,y, (r, g, b))
time.sleep(2)






sense.clear()
