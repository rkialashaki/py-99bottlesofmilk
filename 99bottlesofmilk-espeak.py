#!/usr/bin/env python
import time
from os import system # uses espeak command line utility with system

def take_1_down():
    bottles_milk = 99
    while bottles_milk > 0:
        bottles_milk_minus_1 = bottles_milk - 1
        if bottles_milk == 1:
            system("espeak -s 240 '%s bottle of milk on the wall'" % bottles_milk)
            system("espeak -s 240 '%s bottle of milk'" % bottles_milk)
        else:
            system("espeak -s 240 '%s bottles of milk on the wall'" % bottles_milk)
            system("espeak -s 240 '%s bottles of milk'" % bottles_milk)
        system("espeak -s 240 'Take 1 down pass it around'")
        if bottles_milk_minus_1 == 1:
            system("espeak -s 240 '%s bottle of milk on the wall'" % bottles_milk_minus_1 )
        elif bottles_milk_minus_1 == 0:
            system("espeak -s 240 'No bottles of milk on the wall'")
        else:
            system("espeak -s 240 '%s bottles of milk on the wall'" % bottles_milk_minus_1 )
        bottles_milk = bottles_milk - 1
        time.sleep(0)

take_1_down()
