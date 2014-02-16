#!/usr/bin/python

# check for one of the buttons to be pushed, and play the corresponding birdsong

import pifacedigitalio
import pygame

pygame.init()

pfd = pifacedigitalio.PiFaceDigital()

print "Ready"

lastinp = 0


def play(inp):

    if (inp == 1):
#        print "play hawk"
        pygame.mixer.music.load("hawk.mp3")
        pygame.mixer.music.play()

    if (inp == 2):
#        print "play lark"
        pygame.mixer.music.load("meadowlark.mp3")
        pygame.mixer.music.play()

    if (inp == 3 or inp == 4): # 3rd switch is input 4
#        print "play quail"
        pygame.mixer.music.load("quail.mp3")
        pygame.mixer.music.play()

    if (inp == 8):
#        print "stop"
        pygame.mixer.music.stop()

while 1:

    inp =  pfd.input_port.value

    if (inp != lastinp): # state change

        pfd.leds[lastinp-1].turn_off()
        if inp > 0:  pfd.leds[inp-1].turn_on()
        lastinp = inp

        if (inp>0 and inp<9):
            play(inp)



    
