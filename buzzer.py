#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)

#create Buzz function and set initial sounds frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,1000)


#start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.ChangeFrequency(65.4)
Buzz.start(50)
time.sleep(1)
Buzz.stop()



#reset GPIO resources used by script
GPIO.cleanup()
