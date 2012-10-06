

class NotificationHandler:
    def playbackStarted(self):
        pass
    def playbackEnded(self):
        pass
    def playbackPaused(self):
        pass


class MpdNotificationHandler(NotificationHandler):
    _mpd = None
    _policy = None
        
    def __init__(self, mpdclient, policy):
        self._mpd = mpdclient
        self._policy = policy
        
    def playbackStarted(self):
        pass
    def playbackEnded(self):
        pass
    def playbackPaused(self):
        pass