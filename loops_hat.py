#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random
i=0


for i, c in enumerate('Howdy'):
    r = random.randint(0,255)
    x = random.randint(0,255)
    y = random.randint(0,255)
    
    sense.show_letter(c, (r,  x, y))
    print "RBG:", r, x, y
    time.sleep(1)

sense.clear()
