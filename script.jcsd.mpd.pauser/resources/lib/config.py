

class Config:
    def loadMpdConfig(self, addon, mpdconfig):
        mpdconfig.host = addon.getSetting('host')    
        mpdconfig.port = addon.getSetting('port')
        mpdconfig.password = addon.getSetting('password')

    def loadMpdPolicyConfig(self, addon, mpdPolicyConfig):
        mpdPolicyConfig.pauseOnXbmcPlay = addon.getSetting('pauseOnXbmcPlay')
        mpdPolicyConfig.playOnXbmcPaused = addon.getSetting('playOnXbmcPaused')
        mpdPolicyConfig.playOnXbmcStop = addon.getSetting('playOnXbmcStop')
        mpdPolicyConfig.delayPause = float(addon.getSetting('delayPause'))
        mpdPolicyConfig.delayPlay = float(addon.getSetting('delayPlay'))