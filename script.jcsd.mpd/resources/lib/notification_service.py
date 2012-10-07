# -*- coding: utf-8 -*-
""" Handles notifications from XBMC via its own thread and forwards them on to the scrobbler """

import xbmc
import telnetlib
import socket

import simplejson as json
import threading


class NotificationService(threading.Thread):
    """ Receives XBMC notifications and passes them off as needed """

    TELNET_ADDRESS = 'localhost'
    TELNET_PORT = 9090

    _abortRequested = False
    _handler = None
    _notificationBuffer = ""

    def __init__(self, handler):
        self._handler = handler
        threading.Thread.__init__(self)

    def _forward(self, notification):
        """ Fowards the notification recieved to a function on the scrobbler """
        if not ('method' in notification and 'params' in notification and 'sender' in notification['params'] and notification['params']['sender'] == 'xbmc'):
            return
        try:
            if notification['method'] == 'Player.OnStop':
                self._handler.playbackEnded()
            elif notification['method'] == 'Player.OnPlay':
                self._handler.playbackStarted()
            elif notification['method'] == 'Player.OnPause':
                self._handler.playbackPaused()
            elif notification['method'] == 'System.OnQuit':
                self._abortRequested = True
        except Exception as e :
            print "Error whith handler : '%s'"%(e)

    def _readNotification(self, telnet):
        """ Read a notification from the telnet connection, blocks until the data is available, or else raises an EOFError if the connection is lost """
        while True:
            try:
                addbuffer = telnet.read_some()
            except socket.timeout:
                continue

            if addbuffer == "":
                raise EOFError

            self._notificationBuffer += addbuffer
            try:
                data, offset = json.JSONDecoder().raw_decode(self._notificationBuffer)
                self._notificationBuffer = self._notificationBuffer[offset:]
            except ValueError:
                continue

            return data


    def run(self):
        #while xbmc is running
        telnet = telnetlib.Telnet(self.TELNET_ADDRESS, self.TELNET_PORT)

        while not (self._abortRequested or xbmc.abortRequested):
            try:
                data = self._readNotification(telnet)
            except EOFError:
                telnet = telnetlib.Telnet(self.TELNET_ADDRESS, self.TELNET_PORT)
                self._notificationBuffer = ""
                continue
            self._forward(data)

        telnet.close()
        #self._handler.abortRequested = True
