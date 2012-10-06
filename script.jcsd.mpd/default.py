import debug
import sys, os
import xbmcaddon

__scriptid__ = 'script.jcsd.mpd'
__addon__ = xbmcaddon.Addon(id=__scriptid__)

sys.path.append( os.path.join ( __addon__.getAddonInfo('path'), 'resources','lib') )
from config import Config
from mpdconfig import MpdConfig, MpdPolicyConfig
from notification_handler import MpdNotificationHandler
from notification_service import NotificationService



mpdconfig = MpdConfig()
mpdPolicyConfig = MpdPolicyConfig()

config = Config()
config.loadMpdConfig(__addon__, mpdconfig)
config.loadMpdPolicyConfig(__addon__, mpdPolicyConfig)

mpdh = MpdNotificationHandler(mpdconfig, mpdPolicyConfig)
ns = NotificationService(mpdh)

ns.start()
ns.join()
