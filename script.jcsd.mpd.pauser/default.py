from debug import Debug

import sys, os
import xbmcaddon, xbmc


__scriptid__ = 'script.jcsd.mpd.pauser'
xbmc.log(msg="[MPD PAUSER] %s loaded" % (__scriptid__), level=xbmc.LOGERROR)

__addon__ = xbmcaddon.Addon(id=__scriptid__)
sys.path.append(os.path.join (__addon__.getAddonInfo('path'), 'resources', 'lib'))

xbmc.log(msg="[MPD PAUSER] %s started" % (__scriptid__), level=xbmc.LOGERROR)
Debug.launch_remote_debug()

from notification_handler import MpdNotificationHandler
from notification_service import NotificationService

mpdh = MpdNotificationHandler(__addon__)
ns = NotificationService(mpdh)

ns.start()
ns.join()
xbmc.log(msg="[MPD PAUSER] %s stopped" % (__scriptid__))
