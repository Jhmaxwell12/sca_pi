#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

r = random.randint(0,255)
x = random.randint(0,255)
y = random.randint(0,255)
sense.show_letter("H", (r,  x, y))
time.sleep(1)

r = random.randint(0,255)
x = random.randint(0,255)
y = random.randint(0,255)
sense.show_letter("i", (r, x, y))
time.sleep(1)

r = random.randint(0,255)
x = random.randint(0,255)
y = random.randint(0,255)
sense.show_letter("!", (r, x, y))
time.sleep(1)

sense.clear()
