#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

count=1

while count<1000:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    x=random.randint(1,7)
    y=random.randint(1,7)
    sense.set_pixel(x,y, (r, g, b))
    time.sleep(.1)
    sense.clear()
    count=count+1






sense.clear()
