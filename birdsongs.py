#!/usr/bin/python

# check for one of the buttons to be pushed, and play the corresponding birdsong

# Inputs 1-4 are also the PiFace buttons
# button 1: play one of the bird songs
# button 2: volume up
# button 3: volume down
# button 4: save or stop?

# Inputs 5-7 are the remote switch inputs
# input 5: play "quail"
# input 6: play "hawk"
# input 7: play "meadowlark"

import pifacedigitalio
import pygame
from time import sleep
import alsaaudio

#pygame.init()
pygame.mixer.init()
import signal
import sys
 
def signal_handler(signal, frame):
    print 'SIGNAL {}'.format(signal)
    sleep(1)
    pygame.quit()
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)

pfd = pifacedigitalio.PiFaceDigital()

#print "Ready"

lastinp = 8 # unlikely but safe way to start
inpd = {0:0, 1:1, 2:2, 4:3, 8:4, 16:5, 32:6, 64:7, 128:8} # to translate pfd input to something sane

mixer = alsaaudio.Mixer('PCM') 
volume = int(mixer.getvolume()[0])

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

song = 1

def setvol(vol):
    global mixer
    print 'setvol {}'.format(vol)
    mixer.setvolume(vol)
    print 'getvol {}'.format(mixer.getvolume()[0])


def sing(song):
    print 'sing {}'.format(song)
    if song == 1:
        print "play quail"
        pygame.mixer.music.load("quail.mp3")
        pygame.mixer.music.play()
    elif song == 2:
        print "play hawk"
        pygame.mixer.music.load("hawk.mp3")
        pygame.mixer.music.play()
    elif song == 3:
        print "play lark"
        pygame.mixer.music.load("meadowlark.mp3")
        pygame.mixer.music.play()
    else:
        print "stop"
        pygame.mixer.music.stop()

def play(inp):
    global song, volume

    print 'play {}'.format(inp)

    if (inp == 1):
        sing(song)
        song += 1
        if song > 3: song = 1 # wrap

    elif (inp == 2):
        volume += 1
        setvol(volume)

    elif (inp == 3):
        volume -= 1
        setvol(volume)

    elif (inp == 4):
        print "stop"
        pygame.mixer.music.stop()

    elif (inp >= 5 and inp <= 7):
        sing(inp - 4)

while True:

  try:
    inp = inpd[pfd.input_port.value]

    if (inp != lastinp): # state change
#        print "inp {}".format(inp)

        pfd.leds[lastinp-1].turn_off()
        if inp > 0:  pfd.leds[inp-1].turn_on()
        lastinp = inp

        if (inp>0 and inp<9):
            play(inp)

    sleep(0.1)

  except (KeyboardInterrupt, SystemExit):
    raise

  except:
    pass


