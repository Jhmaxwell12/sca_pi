#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

speed=0
s = "Hello World!" 
a = "You Win"
b= "You Lose"
r=(255, 255, 255)
i=0
guess_num=0
print "You have 10 guesses"
while i < 1:
    speed = speed + .0025
    sense.show_message(s, speed, text_colour=r)
    guess = raw_input("Enter the sentence: ")
    if guess == "Hello World!":
        print 'You win'
        sense.show_message(a, text_colour=r)
        i=i+1
    if guess_num == 9:
        print 'You lose'
        sense.show_message(b, text_colour=r)
        i=i+1
    else:
        print 'Try again'
        guess_num=guess_num+1
sense.clear()
