

class NotificationHandler:
    def playbackStarted(self):
        pass
    def playbackEnded(self):
        pass
    def playbackPaused(self):
        pass


class MpdNotificationHandler(NotificationHandler):
    _mpdconfig = None
    _mpd = None
    _policy = None
        
    def __init__(self, mpdconfig, policy):
        self._mpdconfig = mpdconfig
        self._policy = policy
        
    def playbackStarted(self):
        print "Playback started"
    def playbackEnded(self):
        print "Playback Ended"
    def playbackPaused(self):
        print "Playback paused"