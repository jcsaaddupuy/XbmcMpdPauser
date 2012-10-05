import sys, time
import xbmc


while (not xbmc.abortRequested):
    if xbmc.Player.isPlaying():
        print "Playing"
    else:
        print "Not playing"
    time.sleep(2)