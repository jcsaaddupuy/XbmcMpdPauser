import debug
import sys, os
import xbmcaddon

__scriptid__ = 'script.jcsd.mpd'
__addon__ = xbmcaddon.Addon(id=__scriptid__)

sys.path.append( os.path.join ( __addon__.getAddonInfo('path'), 'resources','lib') )


from notification_handler import MpdNotificationHandler
from notification_service import NotificationService






mpdh = MpdNotificationHandler(__addon__)
ns = NotificationService(mpdh)

ns.start()
ns.join()
