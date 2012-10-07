

class Config:
    def loadMpdConfig(self, addon, mpdconfig):
        mpdconfig.host = addon.getSetting('host')    
        mpdconfig.port = addon.getSetting('port')
        mpdconfig.password = addon.getSetting('password')
        print mpdconfig.host
        print mpdconfig.port
        print mpdconfig.password
    def loadMpdPolicyConfig(self, addon, mpdPolicyConfig):
        mpdPolicyConfig.pauseOnXbmcPlay = True
        mpdPolicyConfig.playOnXbmcPaused = False
        mpdPolicyConfig.playOnXbmcStop = True