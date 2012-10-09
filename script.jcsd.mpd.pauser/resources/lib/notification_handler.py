import time
from mpd import (MPDClient, CommandError)
from socket import error as SocketError

from debug import Debug
from config import Config
from mpdconfig import MpdConfig, MpdPolicyConfig

d=Debug()
class NotificationHandler:
    def playbackStarted(self):
        pass
    def playbackEnded(self):
        pass
    def playbackPaused(self):
        pass


class MpdNotificationHandler(NotificationHandler):
    _addon = None
    _mpdconfig = None
    _mpd = None
    _policy = None
    _config = None
    _mpdconfig = None
    _policy = None
    _wasPaused = None
    
    def __init__(self, addon):
        self._addon = addon
        self._config = Config()
        self._policy = MpdPolicyConfig()
        self._mpdconfig = MpdConfig()
        self._wasPaused = False
        
    def loadconfig(self):
        self._config.loadMpdConfig(self._addon, self._mpdconfig)
        self._config.loadMpdPolicyConfig(self._addon, self._policy)

    def playbackStarted(self):
        d.Log("Playback started")
        client = self.getClient()
        if client is not None:
            if client.status()['state'] == 'play' and self._policy.pauseOnXbmcPlay:
                time.sleep(self._policy.delayPause)
                client.pause()
                self._wasPaused = True
                d.Log("MPD Paused")
                
    def playbackEnded(self):
        d.Log("Playback Ended")
        client = self.getClient()
        if client is not None:
            if self._wasPaused :
                if client.status()['state'] == 'pause' and self._policy.playOnXbmcStop:
                    time.sleep(self._policy.delayPlay)
                    client.play()
                    d.Log("MPD Play")
                self._wasPaused = False
    def playbackPaused(self):
        d.Log("Playback paused")
        client = self.getClient()
        if client is not None:
            if self._wasPaused :
                if client.status()['state'] == 'pause' and self._policy.playOnXbmcPaused:
                    time.sleep(self._policy.delayPlay)
                    client.play()
                    d.Log("MPD Play")
                self._wasPaused = False
                
    def getClient(self):
        self.loadconfig()
        client = MPDClient()
        if self.mpdConnect(client):
            d.Log('Got connected!')
            return client
        else:
            d.Log('Failed to connect MPD server.')
        return None
    
    def mpdConnect(self, client):
        """
        Simple wrapper to connect MPD.
        """
        try:
            con_id = {'host':self._mpdconfig.host, 'port':self._mpdconfig.port}
            client.connect(**con_id)
            if len(self._mpdconfig.password) > 0:
                try:
                    client.password(self._mpdconfig.password)
                except CommandError:
                    d.Log( "Error while authentication")
                    raise
        except SocketError, (e,s):
            d.Log(s)
            return False
        except CommandError, (e,s):
            d.Log(s)
            return False
        except Exception , (e,s):
            d.Log(s)
            return False
        return True
