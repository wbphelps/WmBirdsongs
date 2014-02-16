#!/usr/bin/python

# check for one of the buttons to be pushed, and play the corresponding birdsong

import pifacedigitalio
import pygame
from time import sleep

pygame.init()

hawk = pygame.mixer.Sound("hawk.ogg")
lark = pygame.mixer.Sound("meadowlark.ogg")
quail = pygame.mixer.Sound("quail.ogg")

pfd = pifacedigitalio.PiFaceDigital()

#print "Ready"
i = 0
while i < 8:
    pfd.leds[i].turn_on()
    sleep(0.1)
    i += 1
i = 0
while i < 8:
    pfd.leds[i].turn_off()
    sleep(0.1)
    i += 1

def play(inp):
    global hawk, lark, quail

    hawk.stop()
    quail.stop()
    lark.stop()

    if (inp == 1):
#        print "play hawk"
        hawk.play()

    if (inp == 2):
#        print "play lark"
        lark.play()

    if (inp == 3 or inp == 4): # 3rd switch is input 4
#        print "play quail"
        quail.play()

    if (inp == 8):
#        print "stop"
        pass

lastinp = 0

while 1:

    inp =  pfd.input_port.value

    if (inp != lastinp): # state change

#        print "inp {}".format(inp)

        pfd.leds[lastinp-1].turn_off()
        if inp > 0:  pfd.leds[inp-1].turn_on()
        lastinp = inp

        if (inp>0 and inp<9):
            play(inp)
    
