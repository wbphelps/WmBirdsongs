#!/usr/bin/python

# check for one of the buttons to be pushed, and play the corresponding birdsong

import pifacedigitalio
import pygame
from time import sleep

pygame.init()
import signal
import sys
 
def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)

pfd = pifacedigitalio.PiFaceDigital()

#print "Ready"

lastinp = 8 # unlikely but safe way to start
inpd = {0:0, 1:1, 2:2, 4:3, 8:4, 16:5, 32:6, 64:7, 128:8} # to translate pfd input to something sane

pygame.mixer.music.load("quail.mp3")
pygame.mixer.music.play()

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

pygame.mixer.music.stop()


def play(inp):

    if (inp == 1):
#        print "play quail"
        pygame.mixer.music.load("quail.mp3")
        pygame.mixer.music.play()

    elif (inp == 2):
#        print "play hawk"
        pygame.mixer.music.load("hawk.mp3")
        pygame.mixer.music.play()

    elif (inp == 3):
#        print "play lark"
        pygame.mixer.music.load("meadowlark.mp3")
        pygame.mixer.music.play()

    elif (inp == 4):
#        print "stop"
        pygame.mixer.music.stop()

while 1:

  try:
    inp = inpd[pfd.input_port.value]

    if (inp != lastinp): # state change
#        print "inp {}".format(inp)

        pfd.leds[lastinp-1].turn_off()
        if inp > 0:  pfd.leds[inp-1].turn_on()
        lastinp = inp

        if (inp>0 and inp<9):
            play(inp)

  except:
    pass


    
