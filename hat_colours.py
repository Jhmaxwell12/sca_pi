#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
y= (148, 0, 211)
x=(255, 215, 0)

speed = .05

message = "Hello World"

sense.show_message(message, speed, text_colour=y, back_colour=x)

sense.clear()
