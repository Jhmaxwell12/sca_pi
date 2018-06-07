#!/usr/bin/env python

x = raw_input('Enter first number: ')
y = raw_input('Enter second number: ')
x = int(x)
y = int(y)
if x > y:
    print 'The maximum is:', x
    print 'The minimum is:', y
    print 'Maximum - minimum is:', int(x)-int(y)
else:
    print 'The maximum is:', y
    print 'The minimum is:', x
    print 'Maximum - minimum is:', int(y)-int(x)
