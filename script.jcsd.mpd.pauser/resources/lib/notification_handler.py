import time
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
import xbmc
from config import Config
from mpdconfig import MpdConfig, MpdPolicyConfig


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
        xbmc.log("[MPD PAUSER] Playback started")
        client = self.getClient()
        if client is not None:
            if client.status()['state'] == 'play' and self._policy.pauseOnXbmcPlay:
                time.sleep(self._policy.delayPause)
                client.pause()
                self._wasPaused = True
                xbmc.log("[MPD PAUSER] MPD Paused")
                
    def playbackEnded(self):
        xbmc.log("[MPD PAUSER] Playback Ended")
        client = self.getClient()
        if client is not None:
            if self._wasPaused :
                if client.status()['state'] == 'pause' and self._policy.playOnXbmcStop:
                    time.sleep(self._policy.delayPlay)
                    client.play()
                    xbmc.log("[MPD PAUSER] MPD Play")
                self._wasPaused = False
    def playbackPaused(self):
        xbmc.log("[MPD PAUSER] Playback paused")
        client = self.getClient()
        if client is not None:
            if self._wasPaused :
                if client.status()['state'] == 'pause' and self._policy.playOnXbmcPaused:
                    time.sleep(self._policy.delayPlay)
                    client.play()
                    xbmc.log("[MPD PAUSER] MPD Play")
                self._wasPaused = False
                
    def getClient(self):
        self.loadconfig()
        client = MPDClient()
        if self.mpdConnect(client):
            xbmc.log("[MPD PAUSER] Got connected!")
            return client
        else:
            xbmc.log("[MPD PAUSER] Failed to connect MPD server.")
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
                    xbmc.log("[MPD PAUSER] Error while authentication", level=xbmc.LOGERROR)
                    raise
        except SocketError, (e,s):
            xbmc.log("[MPD PAUSER] %s"%(s), level=xbmc.LOGERROR)
            return False
        except CommandError, (e,s):
            xbmc.log("[MPD PAUSER] %s"%(s), level=xbmc.LOGERROR)
            return False
        except Exception , (e,s):
            xbmc.log(s, level=xbmc.LOGSEVERE)
            return False
        return True
