from debug import Debug

import sys, os
import xbmcaddon

__scriptid__ = 'script.jcsd.mpd.pauser'
__addon__ = xbmcaddon.Addon(id=__scriptid__)
sys.path.append(os.path.join (__addon__.getAddonInfo('path'), 'resources', 'lib'))

Debug.init_log()
Debug.launch_remote_debug()

d = Debug
d.info("%s started" % (__scriptid__))


from notification_handler import MpdNotificationHandler
from notification_service import NotificationService

mpdh = MpdNotificationHandler(__addon__)
ns = NotificationService(mpdh)

ns.start()
ns.join()
d.Log("%s stopped" % (__scriptid__))
