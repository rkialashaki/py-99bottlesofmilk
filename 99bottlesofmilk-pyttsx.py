#!/usr/bin/env python
import time
import pyttsx

engine = pyttsx.init()

def take_1_down():
    bottles_milk = 99
    while bottles_milk > 0:
        bottles_milk_minus_1 = bottles_milk - 1
        if bottles_milk == 1:
            engine.say('%s bottle of milk on the wall' % bottles_milk)
            engine.say('%s bottle of milk' % bottles_milk)
        else:
            engine.say('%s bottles of milk on the wall' % bottles_milk)
            engine.say('%s bottles of milk' % bottles_milk)
        engine.say('Take 1 down pass it around')
        if bottles_milk_minus_1 == 1:
            engine.say('%s bottle of milk on the wall' % bottles_milk_minus_1 )
        elif bottles_milk_minus_1 == 0:
            engine.say('No bottles of milk on the wall')
        else:
            engine.say('%s bottles of milk on the wall' % bottles_milk_minus_1 )
        bottles_milk = bottles_milk - 1
        time.sleep(0)

take_1_down()
engine.runAndWait()

